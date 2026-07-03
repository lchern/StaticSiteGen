import os

from htmlnode import *
from markdown import *


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("ERROR: Level 1 header is missing in the markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as file:
        from_content = file.read()

    with open(template_path) as file:
        template_content = file.read()

    html_string = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string))
