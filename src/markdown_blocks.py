from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):

    PARAGRAPH = 'paragraph'
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"

def block_to_block_type(block):
    """detects what the block type is"""
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH 


def markdown_to_blocks(markdown):
    """Converts a raw markdown string to blocks of strings"""
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            cleaned_blocks.append(block)

    return  cleaned_blocks


def markdown_to_html_node(markdown):
    """Converts markdown to html"""

    blocks = markdown_to_blocks(markdown)

    blocks_list = []

    for block in blocks:
        block_type = block_to_block_type(block) 
        blocks_list.append(block_node(block, block_type))

    return ParentNode('div',blocks_list)
        

def text_to_children(text):
    text = text.replace('\n', ' ')
    text_nodes = text_to_textnodes(text)

    child_list = []

    for text_node in text_nodes:
         child_list.append(text_node_to_html_node(text_node))

    return child_list

    

def block_node(block, block_type):

    if block_type == BlockType.CODE:
        if not block.startswith("```") or not block.endswith("```"):
            raise ValueError("invalid code block")
        block = block.replace("\n","",1)
        block = block.replace("```","")
        return ParentNode("pre",[text_node_to_html_node(TextNode(block, TextType.CODE))])

    if block_type == BlockType.PARAGRAPH:
        child_nodes = text_to_children(block)
        return ParentNode('p',child_nodes)

    elif block_type == BlockType.HEADING:
        x = block.count('#')

        if x + 1 >= len(block):
            raise ValueError(f"invalid heading level: {x}")

        child_nodes = text_to_children(block.replace(f'{x*"#"} ',""))
        return ParentNode(f'h{x}',child_nodes)

    elif block_type == BlockType.QUOTE:
        child_nodes = text_to_children(block.replace('> ',""))
        return ParentNode("blockquote",child_nodes)
    
    elif block_type == BlockType.ULIST:
        
        block_list = []

        list_items = block.split('\n')

        for list_item in list_items:
            list_item = list_item.replace('- ','')
            child_item = text_to_children(list_item)
            block_list.append(ParentNode("li",child_item))

        return ParentNode("ul",block_list)
    
    elif block_type == BlockType.OLIST:
        block_list = []

        list_items = block.split('\n')
        i = 1
        for list_item in list_items:
            list_item = list_item.replace(f'{i}. ','')
            child_item = text_to_children(list_item)
            block_list.append(ParentNode("li",child_item))
            i += 1

        return ParentNode("ol",block_list)
    
    raise ValueError("Invalid block type")
    
    


