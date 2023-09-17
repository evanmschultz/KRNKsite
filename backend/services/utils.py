def remove_after_references(text: str) -> str:
    """
    Remove all text after a line containing the word 'References'.

    Args:
        text (str): The input text.

    Returns:
        str: The text truncated after the line containing 'References'.
    """
    lines: list[str] = text.split("\n")
    for i, line in enumerate(lines):
        if "references" in line.lower():
            return "\n".join(lines[: i + 1])
    return text
