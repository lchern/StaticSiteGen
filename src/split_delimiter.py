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
            split = old_node.text.split(delimiter)
            if len(split) % 2 == 0:
                raise Exception(
                    "Invalid markdown syntax: closing delimiter doesn't exist"
                )
            for i, value in enumerate(split):
                if value == "":
                    continue
                if i % 2 == 0:
                    locally_split.append(TextNode(value, TextType.TEXT))
                else:
                    locally_split.append(TextNode(value, text_type))
            new_nodes.extend(locally_split)
    return new_nodes
