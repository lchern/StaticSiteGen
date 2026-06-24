import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from split import *
from textnode import *


class TestSplitDelimiter(unittest.TestCase):

# Tests for splitting text 
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

# Tests for splitting images and links
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link to [one test site](https://test.site.com) and [another test site](https://test.site.net)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link to ", TextType.TEXT),
                TextNode("one test site", TextType.LINK, "https://test.site.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "another test site", TextType.LINK, "https://test.site.net"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
