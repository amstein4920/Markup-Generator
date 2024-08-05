import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_html(self):
        node1 = HTMLNode(
            "tag",
            "value",
            [HTMLNode("tag1"), HTMLNode("tag2")],
            {
                "href": "https://www.google.com", 
                "target": "_blank",
            })
        self.assertEqual(node1.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_equality_full(self):
        node1 = HTMLNode(
            "tag",
            "value",
            [HTMLNode("tag1"), HTMLNode("tag2")],
            {
                "href": "https://www.google.com", 
                "target": "_blank",
            })
        node2 = HTMLNode(
            "tag",
            "value",
            [HTMLNode("tag1"), HTMLNode("tag2")],
            {
                "href": "https://www.google.com", 
                "target": "_blank",
            })
        self.assertEqual(node1.__repr__(), node2.__repr__())
    
    def test_equality_empty(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1.__repr__(), node2.__repr__())

if __name__ == "__main__":
    unittest.main()