# -*- coding: utf-8 -*-

from .context import eapimt

import unittest


class MonitoringTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def first(self):
        self.assertIsNone()


if __name__ == '__main__':
    unittest.main()