from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value Required")
        
        if not self.tag:
            return str(self.value)
        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        