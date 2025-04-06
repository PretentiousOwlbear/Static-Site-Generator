from textnode import TextNode, TextType
from htmlnode import LeafNode
from create_files import create_files
from generate_page import generate_page


def main():
    create_files()
    generate_page("./content/index.md", "./template.html","./public/index.html")

main()