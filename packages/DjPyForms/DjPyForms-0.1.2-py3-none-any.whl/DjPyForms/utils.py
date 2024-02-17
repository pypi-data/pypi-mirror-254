import os

def confirm_overwrite(filename):
    """
    Asks the user if he wishes to replace an existing file.

    :param filename: Name of the file to check.
    :return: Boolean indicating whether the user wishes to replace the file.
    """
    if os.path.exists(filename):
        response = input(f"The file '{filename}' already exists. Do you want to replace it? (y/n):").lower()
        return response == 'y'
    return True

def create_directory_if_not_exists(directory):
    """
    Creates a directory if it doesn't exist.

    :param directory: Path of the directory to be created.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_or_append_file(filepath, content):
    """
    Creates a file if it doesn't exist, or adds content to the end if it does.
    
    :param filepath: File path.
    :param content: Content to be written to the file.
    """
    mode = 'a' if os.path.exists(filepath) else 'w'
    with open(filepath, mode) as file:
        file.write(content)