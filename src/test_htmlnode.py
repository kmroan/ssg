import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode("a","test",None,{"class":"test"})
        self.assertEqual(node.props_to_html(), " class=\"test\"")

    def test_props_to_html_mutli(self):
        node = HTMLNode("a","test",None,{"href":"https://boot.dev","class":"test","id":"test1"})
        self.assertEqual(node.props_to_html(), " href=\"https://boot.dev\" class=\"test\" id=\"test1\"")

    def test_props_to_html_none(self):
        node = HTMLNode("a","test",None,None)
        self.assertEqual(node.props_to_html(), "")



if __name__ == "__main__":
    unittest.main()
