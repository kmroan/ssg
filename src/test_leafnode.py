import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "test", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.boot.dev\">test</a>")

    def test_to_html_no_props(self):
        node = LeafNode("p", "test")
        self.assertEqual(node.to_html(), "<p>test</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "test")
        self.assertEqual(node.to_html(), "test")

    def test_repr(self):
        node = LeafNode("a", "test", {"href": "https://www.boot.dev"})
        self.assertEqual(repr(node), "LeafNode(a, test, {'href': 'https://www.boot.dev'})")
