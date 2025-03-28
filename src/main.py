from textnode import TextNode, TextType
from htmlnode import LeafNode


def main():

    test = TextNode('This is some anchor text', 'link', 'https://www.boot.dev')
    print(test)

main()