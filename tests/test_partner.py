# -*- coding: utf-8 -*-

from .context import eapimt

import unittest


class CommissioningTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def first(self):
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()
