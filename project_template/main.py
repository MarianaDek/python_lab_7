import pandas as pd
from app.io.input import input_text_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_text_to_console, write_to_file_builtin

def main():
    """
    Main function that calls the input functions to get text,
    prints their outputs to the console, and writes the combined
    results to a file using built-in file handling.
    """
    # Retrieve text from the three input functions
    console_text = input_text_from_console()
    builtin_file_text = read_from_file_builtin()
    pandas_file_text = read_from_file_pandas()

    # Prepare messages for output
    message_console = "Console Input: " + console_text
    message_builtin = "Built-in File Read: " + builtin_file_text
    message_pandas = "Pandas File Read: " + pandas_file_text

    # Output to console
    output_text_to_console(message_console)
    output_text_to_console(message_builtin)
    output_text_to_console(message_pandas)

    # Combine messages for file output
    combined_text = "\n".join([message_console, message_builtin, message_pandas])
    write_to_file_builtin(combined_text)

if __name__ == "__main__":
    main()
