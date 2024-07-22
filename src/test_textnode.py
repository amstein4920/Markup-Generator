import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_none_url(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_text_diff(self):
        node = TextNode("Text 1", "bold", "url")
        node2 = TextNode("Text 2", "bold" "url")
        self.assertNotEqual(node, node2)
    
    def test_type_diff(self):
        node = TextNode("Text", "bold", "url")
        node2 = TextNode("Text", "italics" "url")
        self.assertNotEqual(node, node2)

    def test_url_diff(self):
        node = TextNode("Text", "bold", "url 1")
        node2 = TextNode("Text", "bold", "url 2")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()