# system modules
import os
import re
import pickle
import warnings
import argparse
import importlib
import logging
import sys
import itertools
import fnmatch

# external modules
import matplotlib
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="Show a pickled (and possibly compressed) Matplotlib figure"
)
parser.add_argument("filename", help="the file to open")
args = parser.parse_args()

openers = {}

for module_name, patterns in {
    "lzma": ("*.xz", "*.lzma"),
    "bz2": ("*.bz2", "*.bzip2"),
    "gzip": ("*.gz", "*.gzip"),
    "zstandard": ("*.zst", "*.zstd"),
}.items():
    try:
        module = importlib.import_module(module_name)
        try:
            openers[patterns] = getattr(module, "open")
        except AttributeError:
            logger.warning(
                f"Module '{module_name}' does not have an 'open' function. Ignoring it."
            )
    except ImportError:
        logger.warning(f"No such module '{module_name}'. Ignoring it.")


def cli():
    # TODO: Why is this necessary? matplotlib doesn't do it itself for some reason...
    matplotlib.use(os.environ.get("MPLBACKEND", "TkAgg"))
    opened = 0
    for patterns, opener in itertools.chain(openers.items(), {("*",): open}.items()):
        if not any(fnmatch.fnmatch(args.filename, pattern) for pattern in patterns):
            continue
        try:
            while True:
                reload = False
                with opener(args.filename, "rb") as fh:
                    try:
                        fig = pickle.load(fh)
                    except pickle.UnpicklingError as e:
                        logger.error(f"{type(e).__name__}: {e}")
                        break

                def on_key(event):
                    global reload
                    if event.key == "r":
                        print("reloading!")
                        plt.close("all")
                        reload = True

                cid = fig.canvas.mpl_connect("key_press_event", on_key)
                with warnings.catch_warnings(record=True) as captured_warnings:
                    warnings.simplefilter("always")
                    plt.show()
                    if any(
                        re.search(r"non-interactive.*cannot be shown", str(w.message))
                        for w in captured_warnings
                    ):
                        logger.info(
                            f"Got a non-interactivity warning, so let's try TkAgg backend"
                        )
                        matplotlib.use("TkAgg")
                        plt.show()
                if not reload:
                    sys.exit(0)

        except (ValueError, TypeError) as e:
            logger.error(f"{type(e).__name__}: {e}")
            continue
