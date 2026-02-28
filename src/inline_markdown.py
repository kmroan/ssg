from typing import Text
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

def split_nodes_image(old_nodes):
    res=[]
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            res.append(n)
            continue
        orig = n.text
        img = extract_markdown_images(n.text)
        if len(img) == 0:
            res.append(n)
        for i in img:
            sections = orig.split(f"![{i[0]}]({i[1]})",1)
            if len(sections) != 2:
                raise ValueError("invalid markdown")
            if sections[0] != "":
                res.append(TextNode(sections[0], TextType.TEXT))
            res.append(TextNode(i[0],TextType.IMAGE,i[1]))
            orig = sections[1]
        if orig != "":
            res.append(TextNode(orig, TextType.TEXT))
    return res

def split_nodes_link(old_nodes):
    res=[]
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            res.append(n)
            continue
        orig = n.text
        lnk = extract_markdown_links(orig)
        if len(lnk) == 0:
            res.append(n)
        for i in lnk:
            sections = orig.split(f"[{i[0]}]({i[1]})",1)
            if len(sections) != 2:
                raise ValueError("invalid markdown")
            if sections[0] != "":
                res.append(TextNode(sections[0], TextType.TEXT))
            res.append(TextNode(i[0],TextType.LINK,i[1]))
            orig = sections[1]
        if orig != "":
            res.append(TextNode(orig, TextType.TEXT))
    return res
