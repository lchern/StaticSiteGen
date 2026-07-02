from copy import *

from textnode import TextNode, TextType


def main():
    textnode = TextNode("Dummy Text", TextType.BOLD, "https://www.boot.dev")
    prep_and_copy(Path("static"), Path("public"))


if __name__ == "__main__":
    main()
