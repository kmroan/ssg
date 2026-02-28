import unittest

from inline_markdown import extract_markdown_links, extract_markdown_images

class TestExtract(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is a [link](https://www.boot.dev)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://www.boot.dev")])

    def test_extract_markdown_images(self):
        text = "This is an ![image](https://www.boot.dev/image.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://www.boot.dev/image.png")])