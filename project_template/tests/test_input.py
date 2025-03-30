import os
import pandas as pd
import pytest
from project_template.app.io.input import read_from_file_builtin, read_from_file_pandas

# Automatically change to the temporary directory for each test.
@pytest.fixture(autouse=True)
def change_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)


# Tests for read_from_file_builtin()

def test_read_from_file_builtin_with_content():
    """
    Test that read_from_file_builtin() correctly reads file content.
    """
    filename = "input_builtin.txt"
    expected_content = "Hello world"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(expected_content)

    result = read_from_file_builtin()
    assert result == expected_content


def test_read_from_file_builtin_file_not_found():
    """
    Test that read_from_file_builtin() returns an error message when the file is missing.
    """
    # Ensure the file does not exist.
    if os.path.exists("input_builtin.txt"):
        os.remove("input_builtin.txt")

    result = read_from_file_builtin()
    assert result == "File 'input_builtin.txt' not found."


def test_read_from_file_builtin_empty_file():
    """
    Test that read_from_file_builtin() correctly reads an empty file.
    """
    filename = "input_builtin.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("")

    result = read_from_file_builtin()
    assert result == ""


# Tests for read_from_file_pandas()

def test_read_from_file_pandas_with_data():
    """
    Test that read_from_file_pandas() correctly reads a CSV file with data.
    """
    filename = "input_pandas.csv"
    csv_content = "a,b\n1,2\n3,4\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(csv_content)

    # Create the expected DataFrame string.
    df = pd.read_csv(filename)
    expected = df.to_string()

    result = read_from_file_pandas()
    assert result == expected


def test_read_from_file_pandas_file_not_found():
    """
    Test that read_from_file_pandas() returns an error message when the file is missing.
    """
    if os.path.exists("input_pandas.csv"):
        os.remove("input_pandas.csv")

    result = read_from_file_pandas()
    assert result == "File 'input_pandas.csv' not found."


def test_read_from_file_pandas_empty_csv():
    """
    Test that read_from_file_pandas() correctly reads an empty CSV file (only header).
    """
    filename = "input_pandas.csv"
    csv_content = "a,b\n"  # CSV with header only (empty DataFrame)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(csv_content)

    df = pd.read_csv(filename)
    expected = df.to_string()

    result = read_from_file_pandas()
    assert result == expected