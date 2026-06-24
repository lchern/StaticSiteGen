from extract_markdown import *
from htmlnode import *
from textnode import *


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        locally_split = []
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception(
                    "Invalid markdown syntax: closing delimiter doesn't exist"
                )
            for i, value in enumerate(sections):
                if value == "":
                    continue
                if i % 2 == 0:
                    locally_split.append(TextNode(value, TextType.TEXT))
                else:
                    locally_split.append(TextNode(value, text_type))
            new_nodes.extend(locally_split)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        locally_split = []
        extracted_imgs = extract_markdown_images(original_text)
        if len(extracted_imgs) == 0:
            new_nodes.append(old_node)
            continue
        for i, value in enumerate(extracted_imgs):
            if value == "":
                continue
            sections = original_text.split(
                f"![{extracted_imgs[i][0]}]({extracted_imgs[i][1]})", 1
            )
            if sections[0] != "":
                locally_split.append(TextNode(sections[0], TextType.TEXT))
            locally_split.append(
                TextNode(extracted_imgs[i][0], TextType.IMAGE, extracted_imgs[i][1])
            )
            original_text = sections[1]
        new_nodes.extend(locally_split)
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        locally_split = []
        extracted_links = extract_markdown_links(original_text)
        if len(extracted_links) == 0:
            new_nodes.append(old_node)
            continue
        for i, value in enumerate(extracted_links):
            if value == "":
                continue
            sections = original_text.split(
                f"[{extracted_links[i][0]}]({extracted_links[i][1]})", 1
            )
            if sections[0] != "":
                locally_split.append(TextNode(sections[0], TextType.TEXT))
            locally_split.append(
                TextNode(extracted_links[i][0], TextType.LINK, extracted_links[i][1])
            )
            original_text = sections[1]
        new_nodes.extend(locally_split)
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    original_text = [TextNode(text, TextType.TEXT)]
    original_text = split_nodes_delimiter(original_text, "**", TextType.BOLD)
    original_text = split_nodes_delimiter(original_text, "_", TextType.ITALIC)
    original_text = split_nodes_delimiter(original_text, "`", TextType.CODE)
    original_text = split_nodes_image(original_text)
    original_text = split_nodes_link(original_text)
    return original_text
