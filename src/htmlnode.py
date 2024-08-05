class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"Tag: {self.tag}  Value: {self.value}  Children: {self.children} Props: {self.props}"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        outputString = ""
        if self.props:
            for key, value in self.props.items():
                outputString += f" {key}=\"{value}\""
        return outputString