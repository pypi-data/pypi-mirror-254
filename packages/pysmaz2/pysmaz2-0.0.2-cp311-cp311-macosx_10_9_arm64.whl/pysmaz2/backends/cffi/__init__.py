# -*- coding: utf-8 -*-
from pysmaz2.backends.cffi._smaz2 import ffi, lib


def compress(inp: bytes, bufsize: int) -> bytes:
    buf = ffi.new(f"unsigned char[{bufsize}]")
    outlen = lib.smaz2_compress(
        buf, bufsize, ffi.cast("unsigned char*", ffi.from_buffer(inp)), len(inp)
    )
    return ffi.unpack(ffi.cast("char*", buf), outlen)


def compress_into(inp: bytes, out: bytearray) -> int:
    outlen = lib.smaz2_compress(
        ffi.cast("unsigned char*", ffi.from_buffer(out)),
        len(out),
        ffi.cast("unsigned char*", ffi.from_buffer(inp)),
        len(inp),
    )
    return outlen


def decompress(inp: bytes, bufsize: int) -> bytes:
    buf = ffi.new(f"unsigned char[{bufsize}]")
    outlen = lib.smaz2_decompress(
        buf, bufsize, ffi.cast("unsigned char*", ffi.from_buffer(inp)), len(inp)
    )
    return ffi.unpack(ffi.cast("char*", buf), outlen)


def decompress_into(inp: bytes, out: bytearray) -> int:
    outlen = lib.smaz2_decompress(
        ffi.cast("unsigned char*", ffi.from_buffer(out)),
        len(out),
        ffi.cast("unsigned char*", ffi.from_buffer(inp)),
        len(inp),
    )
    return outlen
