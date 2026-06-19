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
        result_text = list(result)
        if self.props == None or self.props == "":
            return ""
        for key in self.props:
            result_text.append(f' {key}="{self.props[key]}"')
        result = "".join(result_text)
        return result

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
