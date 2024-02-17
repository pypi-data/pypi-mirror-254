"""Load file content to text.

Check encoding and load a file to text.

Win
Linux
    apt install libmagic1

py -3.8 -m pip install python-magic-bin
py -3.8 -m pip install python-magic

import magic
magic.from_file("testdata/test.pdf")

original load_textrev
refer to load_paras.py
"""
# pylint: disable=line-too-long, unused-variable, unused-import

from typing import Union  # noqa
from pathlib import Path
import cchardet

# import pytest
from logzero import logger

# from detect_file import detect_file


def loadtext(filepath: Union[Path, str] = "") -> str:
    """Load file context to text.

    Check encoding and load a file to text.
    """
    filepath = Path(filepath)
    if not filepath.is_file():
        logger.error(" file [%s] does not exist or is not a file.", filepath)
        # return None
        raise Exception(f" file [{filepath}] does not exist or is not a file.")

    # encoding = detect_file(filepath)
    encoding = cchardet.detect(filepath.read_bytes()).get("encoding", "utf8")

    if encoding is None:
        raise Exception("cchardet.detect says it's not a text file.")

    # cchardet: 'GB18030', no need for errors="ignore"
    try:
        text = filepath.read_text(encoding=encoding, errors="ignore")
    except Exception as exc:
        logger.error(" Opening %s resulted in errors: %s", filepath, exc)
        raise

    return text
# 
