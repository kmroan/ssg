from typing import Text
from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


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
            continue
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
            continue
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


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes,"**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes 