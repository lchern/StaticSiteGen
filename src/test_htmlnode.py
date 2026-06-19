import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is some text", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        actual_result = node.props_to_html()
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
