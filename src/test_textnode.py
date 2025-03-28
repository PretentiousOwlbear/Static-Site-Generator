import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a url node", TextType.LINK)
        node2 = TextNode("This is a url node", TextType.LINK)
        self.assertEqual(node, node2)

    def test_url_different(self):
        node = TextNode("This is a url node", TextType.LINK,"link")
        node2 = TextNode("This is a url node", TextType.LINK,"verydifferentlink")
        self.assertNotEqual(node, node2)

    def test_url_same(self):
        node = TextNode("This is a url node", TextType.LINK,"link")
        node2 = TextNode("This is a url node", TextType.LINK,"link")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()