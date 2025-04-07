from create_files import create_files
from generate_page import generate_pages_recursive
import sys

content_path = "./content"
template_path = "./template.html"
public_path = "./docs"
static_path = "./static"

def main():
    try:
        basepath = sys.argv[1]
    except IndexError:
        basepath = "/"

    if basepath == "":
        basepath = "/"

    create_files(public_path, static_path)
    print("Generating page . . .")
    generate_pages_recursive(content_path, template_path, public_path, basepath)

main()