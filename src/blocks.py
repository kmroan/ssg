from blocktype import BlockType
import re

def markdown_to_blocks(markdown):
    res = []
    for i in markdown.split("\n\n"):
        if i == "":
            continue
        res.append(i.strip())
    return res

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


