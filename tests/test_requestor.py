# -*- coding: utf-8 -*-

from .context import eapimt
from eapimt.enphase import requestor as req

import unittest


class RequestorTestSuite(unittest.TestCase):
    """Advanced test cases."""

    ### req.format_uri() Tests Start ###
    def test_format_uri_0_queries(self):
        slug = "/slug"
        url = req.BASE_URL
        result = req.format_uri(slug)
        self.assertEqual(result, url+slug)

    def test_format_uri_1_queries(self):
        slug = "/slug"
        url = req.BASE_URL
        queries = {"key": "value"}
        result = req.format_uri(slug, **queries)
        self.assertEqual(
            result, 
            url+slug+"?key=value")

    def test_format_uri_2_queries(self):
        slug = "/slug"
        url = req.BASE_URL
        queries = {
            "key1": "value1", 
            "key2": "value2"
        }
        result = req.format_uri(slug, **queries)
        self.assertEqual(
            result, 
            url+slug+"?key1=value1&key2=value2")
    ### req.format_uri() Tests End ###


if __name__ == '__main__':
    unittest.main()