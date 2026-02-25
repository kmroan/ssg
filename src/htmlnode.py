

class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        pass
    
    def props_to_html(self):
        if self.props is None:
            return None
        res = []
        for p in self.props:
            res.append(f"{p}=\"{self.props[p]}\"")
        return " ".join(res)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
