from textnode import TextNode, TextType
from htmlnode import LeafNode
from create_files import create_files
from generate_page import generate_pages_recursive


def main():
    create_files()
    print("Generating page . . .")
    generate_pages_recursive("./content", "./template.html","./public")

main()