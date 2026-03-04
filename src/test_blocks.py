import unittest
from blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from blocktype import BlockType

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "This is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello, world!')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "- This is a list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is a list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

class TestMD2HTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        self.assertEqual(
            node,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_headings(self):
        md = """
        # This is a heading

        ## This is a subheading

        ### This is a subsubheading

        #### This is a subsubsubheading

        ##### This is a subsubsubsubheading

        ###### This is a subsubsubsubsubheading 
        """
        node = markdown_to_html_node(md)
        self.assertEqual(
            node,
            "<div><h1>This is a heading</h1><h2>This is a subheading</h2><h3>This is a subsubheading</h3><h4>This is a subsubsubheading</h4><h5>This is a subsubsubsubheading</h5><h6>This is a subsubsubsubsubheading</h6></div>",
        )
    def test_ordered_list(self):
        md = """
        1. This is a list item
        2. This is another list item
        """
        node = markdown_to_html_node(md)
        self.assertEqual(
            node,
            "<div><ol><li>This is a list item</li><li>This is another list item</li></ol></div>",
        )
    def test_unordered_list(self):
        md = """
        - This is a list item
        - This is another list item
        """
        node = markdown_to_html_node(md)
        self.assertEqual(
            node,
            "<div><ul><li>This is a list item</li><li>This is another list item</li></ul></div>",
        )
    def test_quote(self):
        md = """
        > This is a quote
        """
        node = markdown_to_html_node(md)
        self.assertEqual(
            node,
            "<div><blockquote>This is a quote</blockquote></div>",
        )
if __name__ == "__main__":
    unittest.main()

