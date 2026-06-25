from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    prefixes = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    md_split = markdown.split("\n")
    if md_split[0].startswith(prefixes) and len(md_split) == 1:
        return BlockType.HEADING
    if md_split[0] == '```' and md_split[-1] == '```' and len(md_split) > 1:
        return BlockType.CODE
    if all(line.startswith('>') for line in md_split):
        return BlockType.QUOTE
    if all(line.startswith('- ') for line in md_split):
        return BlockType.UNORDERED_LIST
    for i, line in enumerate(md_split):
        if not line.startswith(f"{i + 1}. "):
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST


def markdown_to_blocks(markdown):
    result = markdown.split("\n\n")
    result_stripped = []
    for i in range(len(result)):
        if result[i] != "":
            result_stripped.append(result[i].strip())
    return result_stripped
