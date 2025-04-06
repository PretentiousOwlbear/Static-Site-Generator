from markdown_blocks import markdown_to_html_node, markdown_to_blocks, block_to_block_type, BlockType
import os


def generate_page(from_path, template_path, dest_path):
    '''generates the page'''
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path,'r')
    template_file = open(template_path,'r')
    dest_file = open(dest_path,'w')

    markdown_txt = markdown_file.read()
    markdown_file.close()
    template_txt = template_file.read()
    template_file.close()

    markdown_html = markdown_to_html_node(markdown_txt).to_html()
    title = extract_title(markdown_txt)

    template_txt = template_txt.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html)

    dir = os.path.dirname(dest_path)

    if not os.path.exists(dir):
        os.makedirs(dir)
    
    dest_file.write(template_txt)
    dest_file.close()



def extract_title(markdown):
    """extracts the title from the markdown"""
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            lines = block.split("\n")
            for line in lines:
                if line.startswith('# '):
                    return line.replace("# ", "").strip()
    
    raise Exception("No title found")


