from typing import List


def prepend_lines_to_file(file_path: str, lines_to_prepend: List[str]):
    """
    Add a list of lines to the beginning of a file.
    """

    for line in lines_to_prepend[::-1]:
        with open(file_path, "r+", encoding="utf-8") as file:
            content = file.read()
            file.seek(0, 0)
            file.write(line.rstrip("\r\n") + "\n" + content)
