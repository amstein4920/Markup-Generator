import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_p_tag_html(self):
        leaf = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

    def test_a_tag_html(self):
        leaf = LeafNode(tag="a",
                        value="Click me!",
                        props={"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_props(self):
        leaf = LeafNode(tag="a",
                        value="Click me!",
                        props={"href": "https://www.google.com"})
        self.assertEqual(leaf.props_to_html(), " href=\"https://www.google.com\"")

if __name__ == "__main__":
    unittest.main()