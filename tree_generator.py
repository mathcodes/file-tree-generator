import os
###
#  The os module in Python provides a way to interact with the underlying operating system in a portable manner. It offers various functions and methods for working with files and directories, environment variables, processes, and more.
# In this context, os is an abbreviation for "operating system". The module allows you to perform operations such as navigating through directories, creating and deleting files, getting information about files, executing system commands, and other operating system-related tasks
# Here are a few examples of what you can do with the os module:

# Get the current working directory: os.getcwd()
# Create a directory: os.mkdir(path)
# List files and directories in a directory: os.listdir(path)
# Check if a file or directory exists: os.path.exists(path)
# Join multiple parts of a file path: os.path.join(path1, path2, ...)
# Execute a system command: os.system(command)
# Get information about a file: os.stat(path)
###

def format_tree(tree, indent_char='|   ', last_indent_char='└── ', empty_indent_char='    '):
    """
    Now let's format the tree structure with the following parameters.
    tree: The tree structure to format.
    indent_char: The character(s) used for indentation.
    last_indent_char: The character(s) used for the last indentation level.
    empty_indent_char: The character(s) used for empty indentation.
    :return: The formatted tree structure.
    """
    lines = tree.strip().split('\n')  # Split the tree structure into lines
    formatted_lines = []  # Create an empty list to store the formatted lines

    # Determine the minimum indentation level
    min_indent = min(len(line) - len(line.strip()) for line in lines if line.strip())
# min_indent: This variable stores the minimum indentation level among the lines of the tree structure.

# min(): This is a Python built-in function used to find the minimum value among a sequence of values.

# len(line): This expression calculates the length of a line (number of characters) in the tree structure.

# len(line.strip()): This expression calculates the length of a line after removing leading and trailing whitespace. It trims any spaces, tabs, or newline characters from the beginning and end of the line.

# for line: This is a part of a loop statement that iterates over each item (line) in a collection.

# in lines: This specifies the collection (list, tuple, etc.) from which the loop iterates. In this case, it iterates over the lines variable, which represents the lines of the tree structure.

# if line.strip(): This is a conditional statement that checks if the stripped version of a line (with leading and trailing whitespace removed) is non-empty. It filters out lines that are empty or contain only whitespace.

# In summary, the code iterates over each line in the lines collection, calculates the difference between the length of each line and the length of the stripped version (with whitespace removed), and finds the minimum value among these differences using the min() function. The resulting minimum indentation is stored in the min_indent variable.
    # Iterate over each line in the tree structure
    for line in lines:
        # Calculate the indent level based on the indentation characters
        indent_level = (len(line) - len(line.lstrip()) - min_indent) // len(indent_char) + 1
        formatted_line = line.strip()  # Remove leading/trailing whitespace

        # Add appropriate indentation based on the indent level
        if indent_level > 0:
            formatted_line = indent_char * (indent_level - 1) + last_indent_char + formatted_line

        formatted_lines.append(formatted_line)  # Append the formatted line to the list

    formatted_tree = '\n'.join(formatted_lines)  # Join the formatted lines with newline characters
    return formatted_tree  # Return the formatted tree structure

def get_directory_tree(directory):
    """
    Generates the directory tree structure for the given directory.`
    directory: The directory path.
    :return: The directory tree structure.
    """
    tree_structure = ""  # Create an empty string to store the tree structure

    # Iterate over the files and directories in the given directory
    for root, dirs, files in os.walk(directory):
        # Calculate the current indentation level
        current_level = root.count(os.sep) - directory.count(os.sep)

        # Generate the indentation string based on the current level
        indent = "|   " * current_level

        # Append the formatted directory name
        tree_structure += f"{indent}{os.path.basename(root)}\n"

        # Generate the indentation string for subdirectories/files
        subindent = "|   " * (current_level + 1)

        # Append the formatted file names
        for file in files:
            tree_structure += f"{subindent}{file}\n"

    return tree_structure  # Return the generated tree structure

# Get the current directory
current_directory = os.getcwd()  # Get the current working directory

# Generate the directory tree structure
tree_structure = get_directory_tree(current_directory)  # Generate the tree structure for the current directory

# Format the directory tree
formatted_tree = format_tree(tree_structure)  # Format the tree structure with appropriate indentation

# Ask the user for the file name to create
file_name = input("Enter the file name to create (including extension): ")  # Prompt the user to enter the file name

# Create the file with the tree structure
with open(file_name, "w") as f:  # Open the file in write mode
    f.write(formatted_tree)  # Write the formatted tree structure to the file

print(f"The file '{file_name}' has been created with the directory tree structure.")  # Print the confirmation message
