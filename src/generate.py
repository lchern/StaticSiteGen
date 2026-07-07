import os
from pathlib import Path

from htmlnode import *
from markdown import *


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("ERROR: Level 1 header is missing in the markdown")


# DEPRECATED
#
# def generate_page(from_path, template_path, dest_path):
#    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
#
#    with open(from_path) as file:
#        from_content = file.read()
#
#    with open(template_path) as file:
#        template_content = file.read()
#
#    html_string = markdown_to_html_node(from_content).to_html()
#    title = extract_title(from_content)
#    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
#    with open(dest_path, "w") as file:
#        file.write(template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string))


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(
        f"Generating pages recursively from {dir_path_content} to {dest_dir_path} using {template_path}, basepath is {basepath}"
    )
    contents = os.listdir(dir_path_content)
    for item in contents:
        if os.path.isfile(os.path.join(dir_path_content, item)):
            if Path(item).suffix == ".md":
                with open(os.path.join(dir_path_content, item)) as file:
                    from_content = file.read()

                with open(template_path) as file:
                    template_content = file.read()

                html_string = markdown_to_html_node(from_content).to_html()
                title = extract_title(from_content)
                os.makedirs(dest_dir_path, exist_ok=True)
                with open(
                    os.path.join(dest_dir_path, item.replace(".md", ".html")), "w"
                ) as file:
                    file.write(
                        template_content.replace("{{ Title }}", title)
                        .replace("{{ Content }}", html_string)
                        .replace('href="/', f'href="{basepath}')
                        .replace('src="/', f'src="{basepath}')
                    )
        else:
            generate_pages_recursive(
                os.path.join(dir_path_content, item),
                template_path,
                os.path.join(dest_dir_path, item),
                basepath,
            )
