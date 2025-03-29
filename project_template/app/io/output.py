def output_text_to_console(text):
    """
    Outputs text to the console.

    Prints the provided text to the terminal.

    Args:
        text (str): The text to be output.
    """
    print(text)


def write_to_file_builtin(text):
    """
    Writes data to a file using Python's built-in file handling.

    Writes the provided text to the file 'output.txt'.

    Args:
        text (str): The text to be written to the file.
    """
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)
