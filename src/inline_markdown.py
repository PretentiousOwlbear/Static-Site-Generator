from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Splits given nodes text with given markdown"""
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        node_list = []

        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0: 
            raise ValueError(f"Closing delimeter: {delimiter} not found")

        for x in range(len(split_text)):
            if split_text[x] == "":
                continue
            if x % 2 == 0:
                node_list.append(TextNode(split_text[x],TextType.TEXT))
                  
            else:
                node_list.append(TextNode(split_text[x],text_type))
                
        new_nodes.extend(node_list)
    return new_nodes


def extract_markdown_images(text):
    """extracts image markdown from text"""
    return  re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text): 
    """extracts link markdown from text"""
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)


def split_nodes_image(old_nodes):
    """Splits image markdown into its own node with given nodes text"""

    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if len(images) == 0:
            new_nodes.append(node)
            continue
       
        for image in images:
        
            sections = text.split(f'![{image[0]}]({image[1]})',1)

            if len(sections) != 2: 
                raise ValueError(f"image section not closed")


            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            
            new_nodes.append(TextNode(image[0], TextType.IMAGE,image[1]))

            text = sections[1]

        if text != "":
            new_nodes.append(TextNode(text,TextType.TEXT))
   
    return new_nodes
    


def split_nodes_link(old_nodes):
    """Splits link markdown into its own node with given nodes text"""

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

       
        for link in links:
        
            sections = text.split(f'[{link[0]}]({link[1]})',1)

            if len(sections) != 2: 
                raise ValueError(f"Link section not closed")


            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            
            new_nodes.append(TextNode(link[0], TextType.LINK,link[1]))

            text = sections[1]

        if text != "":
            new_nodes.append(TextNode(text,TextType.TEXT))
        
        
    return new_nodes
    

def text_to_textnodes(text):
    """Converts text to text node using all functions in file"""

    text_node = [TextNode(text, TextType.TEXT)]
    text_node = split_nodes_link(text_node)
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_delimiter(text_node, '**', TextType.BOLD)
    text_node = split_nodes_delimiter(text_node, '_', TextType.ITALIC)
    text_node = split_nodes_delimiter(text_node, "`", TextType.CODE)

    return text_node




