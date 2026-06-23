import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from split_delimiter import *
from textnode import *


class TestSplitDelimiter(unittest.TestCase):
    def test_split_italic(self):
        node = TextNode("This is some _italic text_ within plain text", TextType.TEXT)
        actual_result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_result = [
            TextNode("This is some ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" within plain text", TextType.TEXT),
        ]
        self.assertEqual(actual_result, expected_result)

    def test_split_bold(self):
        node = TextNode("This is some **bold text** within plain text", TextType.TEXT)
        actual_result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_result = [
            TextNode("This is some ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" within plain text", TextType.TEXT),
        ]
        self.assertEqual(actual_result, expected_result)

    def test_split_beginning(self):
        node = TextNode("**Bold text** is in the beginning of a line", TextType.TEXT)
        actual_result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_result = [
            TextNode("Bold text", TextType.BOLD),
            TextNode(" is in the beginning of a line", TextType.TEXT),
        ]
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
