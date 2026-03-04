from blocktype import BlockType
from htmlnode import HTMLNode,ParentNode, LeafNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    if re.match(r"#{1,6}", block):
        return BlockType.HEADING
    if re.match(r"^```.*```$",block,re.DOTALL):
        return BlockType.CODE
    if re.match(r"^>",block):
        return BlockType.QUOTE
    if re.match(r"^-\s",block):
        return BlockType.UNORDERED_LIST
    if re.match(r'^\d\.', block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    res = []
    for t in textnodes:
        res.append(text_node_to_html_node(t))
    return res

def heading_to_html_node(heading):
    level = len(re.match(r"#{1,6}", heading).group(0))
    if level < 1 or level > 6:
        raise ValueError("Invalid heading level")
    heading = heading[level+1:]
    nodes = text_to_children(heading)
    return ParentNode(f"h{level}", nodes)

def code_to_html_node(code):
    return ParentNode("pre",[LeafNode("code",code[2:-2])],None)

def quote_to_html_node(quote):
    if not quote.startswith(">"):
        raise ValueError("Invalid quote")
    return ParentNode("blockquote",text_to_children(quote[1:].strip()))

def unordered_list_to_html_node(unordered_list):
    if not unordered_list.startswith("- "):
        raise ValueError("Invalid unordered list")
    res = []
    for l in unordered_list.split("\n"):
        l = l.strip()
        if l == "":
            continue
        if l.startswith("- "):
            l = l[2:]
        res.append(l)
    return ParentNode("ul",[LeafNode("li",r) for r in res])

def ordered_list_to_html_node(ordered_list):
    if not re.match(r'^\d\.', ordered_list):
        raise ValueError("Invalid ordered list")
    res = []
    for l in ordered_list.split("\n"):
        l = l.strip()
        if l == "":
            continue
        if re.match(r'^\d\.', l):
            l = l[3:]
        res.append(l)
    return ParentNode("ol",[LeafNode("li",r) for r in res])

def paragraph_to_html_node(paragraph):
    paragraph = paragraph.split("\n")
    res = []
    for p in paragraph:
        res.append(p.strip())
    return ParentNode("p",text_to_children(' '.join(res)))

def markdown_to_html_node(markdown):
    html = ParentNode("div",[])
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        type = block_to_block_type(b)
        match type:
            case BlockType.HEADING:
                html.children.append(heading_to_html_node(b))
            case BlockType.CODE:
                html.children.append(code_to_html_node(b))
            case BlockType.QUOTE:
                html.children.append(quote_to_html_node(b))
            case BlockType.UNORDERED_LIST:
                html.children.append(unordered_list_to_html_node(b))
            case BlockType.ORDERED_LIST:
                html.children.append(ordered_list_to_html_node(b))
            case BlockType.PARAGRAPH:
                html.children.append(paragraph_to_html_node(b))
            case _:
                raise ValueError(f"Invalid block type: {type}")
    return html.to_html()