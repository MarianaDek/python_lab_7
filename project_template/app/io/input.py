import pandas as pd

def input_text_from_console():
    """
    Reads text input from the console.

    Prompts the user to enter text and returns the entered string.

    Returns:
        str: The text entered by the user.
    """
    return input("Please enter some text: ")


def read_from_file_builtin():
    """
    Reads data from a file using Python's built-in file handling.

    Opens the file 'input_builtin.txt', reads its content, and returns it.
    If the file does not exist, returns an error message.

    Returns:
        str: The content of the file or an error message.
    """
    try:
        with open("input_builtin.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "File 'input_builtin.txt' not found."


def read_from_file_pandas():
    """
    Reads data from a file using the pandas library.

    Reads the CSV file 'input_pandas.csv' into a DataFrame and returns its string representation.
    If the file does not exist, returns an error message.

    Returns:
        str: The DataFrame content as a string or an error message.
    """
    try:
        df = pd.read_csv("input_pandas.csv")
        return df.to_string()
    except FileNotFoundError:
        return "File 'input_pandas.csv' not found."

