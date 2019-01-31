"""
Test file for the class JsonToolbox
"""
import unittest

from pyjt.json_toolbox import JsonToolbox


class TestJsonToolbox(unittest.TestCase):
    """Test Json filtering features"""

    def setUp(self):
        self.toolbox = JsonToolbox([], [])

    def test_process_json_simple(self):
        """> Test filtering of a json object"""
        d = {"foo": "bar", "test": "hello"}
        self.toolbox.to_keep = ["foo"]
        d_ = self.toolbox.process_json(d)
        self.assertIn("foo", d_)
        self.assertNotIn("test", d_)

    def test_process_json_list(self):
        """> Test filtering of an array of json objects"""
        d = [{"foo": "bar", "test": "hello"}]
        self.toolbox.to_keep = ["foo"]
        self.toolbox.process_json(d)
