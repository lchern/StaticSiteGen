from copy import *

from generate import *
from textnode import TextNode, TextType


def main():
    textnode = TextNode("Dummy Text", TextType.BOLD, "https://www.boot.dev")
    prep_and_copy(Path("static"), Path("public"))
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
