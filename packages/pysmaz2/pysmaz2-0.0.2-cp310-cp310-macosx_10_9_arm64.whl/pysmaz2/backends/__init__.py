# -*- coding: utf-8 -*-
import os
import platform

impl = platform.python_implementation()


def _should_use_cffi() -> bool:
    ev = os.getenv("SMAZ2_USE_CFFI")
    if ev is not None:
        return True
    if impl == "CPython":
        return False
    else:
        return True


if not _should_use_cffi():
    from pysmaz2.backends.cython import (
        compress,
        compress_into,
        decompress,
        decompress_into,
    )
else:
    from pysmaz2.backends.cffi import (
        compress,
        compress_into,
        decompress,
        decompress_into,
    )
