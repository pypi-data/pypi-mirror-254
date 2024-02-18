# internal modules
import os
import bz2
import gzip
import lzma
import pickle
import re
import pathlib
import logging
import zstandard

# external modules
import dill
from rich import print
from rich.progress import Progress, BarColumn
import braceexpand

logger = logging.getLogger(__name__)


def save(fig, output, *args, console=None, **kwargs):
    """
    Convenience wrapper around :func:`matplotlib.figure.Figure.savefig` that
    does the following extra steps:

    - do brace-expansion in the given output paths (e.g. ``fig.{png,eps,pdf}``)
    - show progress bar
    - delete the output file if it is a symlink and can't be written to (useful
      for git-annex/datalad)
    - can save to ``.fig.pickle`` or ``fig.dill`` formats with proper
      compression suffix handling
    - defaults to removing the ``CreationDate`` from the output metadata
      (reproducibility!)

    Args:
        fig (matplotlib.figure.Figure): figure to save
        output (str): output path, will be brace-expanded
        console (rich.console.Console, optional): the console to use for the
            progress bar
        *args,**kwargs: further arguments to
            :func:`matplotlib.figure.Figure.savefig()`

    Returns:
        What :func:`matplotlib.figure.Figure.savefig()` would return, or a list
        of it for multiple outputs
    """
    compressors = {
        "gz": gzip.open,
        "gzip": gzip.open,
        "bz2": bz2.open,
        "bzip": bz2.open,
        "bzip2": bz2.open,
        "xz": lzma.open,
        "zst": zstandard.open,
        None: open,
    }
    results = []
    with Progress(
        *Progress.get_default_columns()[::-1],
        console=console,
        transient=True,
    ) as progress:
        outputs = tuple(braceexpand.braceexpand(output))
        task = progress.add_task(f"📥 Saving")
        for output in progress.track(outputs, task_id=task):
            progress.update(task, description=f"📥 Saving to {output!r}")
            if pathlib.Path(output).is_symlink() and not os.access(output, os.W_OK):
                try:
                    logger.info(f"🗑️ Deleting {output!r}")
                    os.remove(output)
                except OSError as e:
                    logger.error(
                        f"💥 Couldn't delete {output!r}: {e}. Trying to save plot anyway."
                    )
            default_savefig_kwargs = dict(metadata={"CreationDate": None})
            if m := re.search(
                r"\.fig\.(?P<serializer>pickle|dill)(?:\.(?P<compression>\w+))?$",
                output,
                flags=re.IGNORECASE,
            ):
                if not (
                    opener := compressors.get(
                        compression := m.groupdict().get("compression")
                    )
                ):
                    logger.warning(
                        f"⚠️ Don't know how to compress {compression!r} file {output!r}. Writing uncompressed."
                    )
                    opener = open
                if not (
                    serializer := {
                        "pickle": pickle.dump,
                        "dill": dill.dump,
                    }.get(serializefmt := m.groupdict().get("serializer"))
                ):
                    logger.warning(
                        f"⚠️ Don't know how to serialize {serializefmt!r} file {output!r}. Using pickle."
                    )
                    serializer = pickle.dump
                with opener(output, "wb") as fh:
                    serializer(fig, fh)
                continue
            if m := re.search(r"\.(?P<format>\w+)$", output, re.IGNORECASE):
                if (fmt := m.groupdict().get("format")) == "svg":
                    default_savefig_kwargs["metadata"].pop("CreationDate", None)
            results.append(
                fig.savefig(output, *args, **{**default_savefig_kwargs, **kwargs})
            )
            logger.info(f"📥 Saved to {output!r}")
        return results[0] if len(results) == 1 else results
