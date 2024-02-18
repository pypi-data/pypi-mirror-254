# -*- coding: utf-8 -*-
import sys
sys.path.append(".")
import os

os.environ["SMAZ2_USE_CFFI"] = "1"

import random
from unittest import TestCase

from pysmaz2 import compress, compress_into, decompress, decompress_into

seed = b"1234567890abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_token(num: int) -> str:
    return b"".join(random.choice(seed).to_bytes(1, "little") for _ in range(num))


class TestSmaz2(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_smaz2_compress(self):
        for i in range(1000):
            data = generate_token(10)
            compressed = compress(data, 100)
            decompressed = decompress(compressed, 100)
            self.assertEqual(data, decompressed)

    def test_smaz2_compress_into(self):
        buf = bytearray(100)
        buf2 = bytearray(100)
        for i in range(1000):
            data = generate_token(10)
            compressed = compress_into(data, buf)
            decompressed = decompress_into(buf[:compressed], buf2)
            self.assertEqual(bytes(buf2[:decompressed]), data)


if __name__ == "__main__":
    import unittest

    unittest.main()
