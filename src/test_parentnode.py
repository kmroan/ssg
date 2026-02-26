import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("div", [LeafNode("p", "test")])
        self.assertEqual(node.to_html(), "<div><p>test</p></div>")

    def test_repr(self):
        node = ParentNode("div", [LeafNode("p", "test")])
        self.assertEqual(repr(node), "ParentNode(div, [LeafNode(p, test, None)], None)")