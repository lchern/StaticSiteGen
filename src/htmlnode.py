class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        if self.props == None or self.props == "":
            return ""
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        result = ""
        if self.tag is None:
            raise ValueError("Invalid HTML: tag is missing")
        if self.children is None:
            raise ValueError("Invalid HTML: children are missing in Parent node")
        for child in self.children:
            result += child.to_html()
        if self.props is None:
            return f"<{self.tag}>{result}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
