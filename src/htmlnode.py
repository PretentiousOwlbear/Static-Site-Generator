class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        """converts props to html"""

        if self.props is None:
            return ""
        
        text = ""
        for prop in self.props:
            text += f' {prop}="{self.props[prop]}"'

        return text
    
    def __repr__(self):

        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag,value, None, props)
        

    def to_html(self):
        """conerts to html format"""
        if self.value is None:
            raise ValueError("HTML invalid: needs a value")
        
        elif self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("HTML invalid: needs a tag")
        
        elif self.children is None:
            raise ValueError("HTML invalid: needs children")

        html = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html += f"{child.to_html()}"


        return html + f"</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    


