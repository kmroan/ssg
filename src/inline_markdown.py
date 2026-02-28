from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    res = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            res.append(n)
            continue
        split = []
        parts = n.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid number of delimiters")
        for p in range(len(parts)):
            if parts[p] == "":
                continue
            if p % 2 == 0:
                split.append(TextNode(parts[p], TextType.TEXT))
            else:
                split.append(TextNode(parts[p], text_type))
        res.extend(split)
    return res


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)