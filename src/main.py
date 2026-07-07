import sys
from copy import *

from generate import *
from textnode import TextNode, TextType


def main():
    basepath = sys.argv[1] if len(sys.argv) >= 2 else "/"
    prep_and_copy(Path("static"), Path("docs"))
#    generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
