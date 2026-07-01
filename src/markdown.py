from enum import Enum
from htmlnode import *
from textnode import *
from split import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    prefixes = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    md_split = markdown.split("\n")
    if md_split[0].startswith(prefixes) and len(md_split) == 1:
        return BlockType.HEADING
    if md_split[0] == '```' and md_split[-1] == '```' and len(md_split) > 1:
        return BlockType.CODE
    if all(line.startswith('>') for line in md_split):
        return BlockType.QUOTE
    if all(line.startswith('- ') for line in md_split):
        return BlockType.UNORDERED_LIST
    for i, line in enumerate(md_split):
        if not line.startswith(f"{i + 1}. "):
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST


def markdown_to_blocks(markdown):
    result = markdown.split("\n\n")
    result_stripped = []
    for i in range(len(result)):
        if result[i] != "":
            result_stripped.append(result[i].strip())
    return result_stripped

#  Below are the helper functions for markdown_to_html_node function

def text_to_children(text):
    list_textnodes = text_to_textnodes(text)
    list_htmlnodes = []
    for textnode in list_textnodes:
        list_htmlnodes.append(text_node_to_html_node(textnode))
    return list_htmlnodes

def paragraph_to_html_node(block):
    edited_block = block.replace("\n", " ")
    text_to_pass = text_to_children(edited_block)
    new_node = ParentNode("p", text_to_pass)
    return new_node

def heading_to_html_node(block):
    counter = block.count("#", 0, 6)
    tag_counted = f"h{counter}"
    edited_block = block.lstrip("#").strip()
    text_to_pass = text_to_children(edited_block)
    new_node = ParentNode(tag_counted, text_to_pass)
    return new_node

def code_to_html_node(block):
    edited_block = block[4:-3]
    new_text_node = TextNode(edited_block, TextType.TEXT)
    converted_node = text_node_to_html_node(new_text_node)
    wrapped_node = ParentNode("code", [converted_node])
    new_node = ParentNode("pre", [wrapped_node])
    return new_node

def quote_to_html_node(block):
    blocks = block.split("\n")
    items = []
    for item in blocks:
        if item != "":
            items.append(item.lstrip(">").strip())
    processed = " ".join(items)
    text_to_pass = text_to_children(processed)
    new_node = ParentNode("blockquote", text_to_pass)
    return new_node

def unordered_list_to_html_node(block):
    items = []
    blocks = block.split("\n")
    for item in blocks:
        if item != "":
            edited_block = item.lstrip("-").strip()
            inner_text_to_pass = text_to_children(edited_block)
            inner_new_node = ParentNode("li", inner_text_to_pass)
            items.append(inner_new_node)
    new_node = ParentNode("ul", items)
    return new_node

def ordered_list_to_html_node(block):
    items = []
    blocks = block.split("\n")
    for item in blocks:
        if item != "":
            edited_block = item.split(". ", 1)
            inner_text_to_pass = text_to_children(edited_block[1])
            inner_new_node = ParentNode("li", inner_text_to_pass)
            items.append(inner_new_node)
    new_node = ParentNode("ol", items)
    return new_node

#  Above are the helper functions for markdown_to_html_node function

def markdown_to_html_node(markdown):
    new_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            new_node = paragraph_to_html_node(block)
        elif block_type == BlockType.HEADING:
            new_node = heading_to_html_node(block)
        elif block_type == BlockType.CODE:
            new_node = code_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            new_node = quote_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            new_node = unordered_list_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            new_node = ordered_list_to_html_node(block)
        else:
            raise ValueError("ERROR: Unrecognized block type")
        new_nodes.append(new_node)
    result = ParentNode("div", new_nodes)
    return result
