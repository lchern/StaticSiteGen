from textnode import TextNode, TextType

def main():
    textnode = TextNode("Dummy Text", TextType.BOLD, "https://www.boot.dev")
    print(textnode)

if __name__ == "__main__":
    main()
