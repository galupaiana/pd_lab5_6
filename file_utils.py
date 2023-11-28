import os

def get_file_size(file_path):
    """Get the file size in bytes.

    Args:
        file_path (str): Path to the file.

    Returns:
        int: File size in bytes or -1 if the file is not found.
    """
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        return -1

def copy_file(source_path, destination_path):
    """Copy content from one file to another.

    Args:
        source_path (str): Path to the source file.
        destination_path (str): Path to the file where the content will be copied.

    Returns:
        str: Message indicating successful completion of the operation or an error message if the file is not found.
    """
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
        return "File successfully copied."
    except FileNotFoundError:
        return "File not found"
