# -*- coding: utf-8 -*-
import glob

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef(
    """
unsigned long smaz2_compress(unsigned char *dst, unsigned long dstlen, unsigned char *s, unsigned long len);
unsigned long smaz2_decompress(unsigned char *dst, unsigned long dstlen, unsigned char *c, unsigned long len);
    """
)

source = """
#include "smaz2.h"
"""
c_sources = ["./dep/smaz2.c"]
print(c_sources)

ffibuilder.set_source(
    "pysmaz2.backends.cffi._smaz2",
    source,
    sources=c_sources,
    include_dirs=["./dep"],
)

if __name__ == "__main__":
    ffibuilder.compile()
