def markdown_to_blocks(markdown):
    result = markdown.split("\n\n")
    result_stripped = []
    for i in range(len(result)):
        if result[i] != "":
            result_stripped.append(result[i].strip())
    return result_stripped
