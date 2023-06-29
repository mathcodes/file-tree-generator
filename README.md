# Directory Tree Generator

Run this Python script in file directories to generate a file tree structure. It will create a file, 'tree.md', with the file tree.

## Table of Contents
- [Directory Tree Generator](#directory-tree-generator)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Files](#files)
    - [powershell\_tree\_generator.ps1](#powershell_tree_generatorps1.ps1)
    - [powershell\_tree\_generator.py](#powershell_tree_generatorpy)
      - [NOTE: Read the comments for a detailed explanation of the code](#note-read-the-comments-for-a-detailed-explanation-of-the-code)
  - [Downloads](#downloads)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Description

This script utilizes Python and PowerShell to generate a file tree structure and store it in a markdown file for easier visualization. It uses the `format_tree` function to format the tree structure and PowerShell to capture the output and assign it to a variable.

## Files

<details>
<summary><strong>powershell_tree_generator.ps1</strong></summary>

```powershell
function Show-Tree($Path = ".", $indent = 0)
{
    Get-ChildItem -Path $Path | ForEach-Object {
        "{0}{1}" -f ("    " * $indent), $_.Name
        if ($_.PSIsContainer) {
            Show-Tree -Path $_.FullName -indent ($indent + 1)
        }
    }
}

Show-Tree
```

</details>

This PowerShell script recursively displays a directory tree structure using indentation. It utilizes the `Show-Tree` function to achieve this functionality.

<details>
<summary><strong>powershell_tree_generator.py</strong></summary>

```python
import os
import subprocess
print(os.getcwd())

# Function to format the tree structure
def format_tree(tree, indent_char='|   ', last_indent_char='└── ', empty_indent_char='    '):

    lines = tree.strip().split('\n')

    formatted_lines = []

    # Determine the minimum indentation level
    min_indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())
    ###
    ## Converted into a for loop so I can print the values as the loop above is a generator expression, which is good for memory but not for debugging
    # min_indent = None
    # for line in lines:
    #     if line.strip():
    #         stripped_line = len(line) - len(line.lstrip())
    #         print(f"Current line stripped length: {stripped_line}")
    #         if min_indent is None or stripped_line < min_indent:
    #             min_indent = stripped_line
    #         print(f"Current min_indent: {min_indent}")

    # print(f"Final min_indent: {min_indent}")
    ###

    # This for loop assigns the indent_level variable to the number of indentations in the line

    for line in lines:
        # the calculation can be explained as follows:
            # // = floor division, which returns the quotient of the division rounded down to the nearest integer
            # indent_level                              = (the number of spaces at the beginning of the line    -   the minimum number of spaces at the beginning of the line)  // the number of spaces in the indent_char variable + 1
            # the number of indentations in the line    = (len(line) - len(line.lstrip())                       -   min_indent)                                                 // len(indent_char)                                 + 1
        indent_level = (len(line) - len(line.lstrip()) - min_indent) // len(indent_char) + 1
        # formatted_line = the line with the spaces at the beginning removed
        formatted_line = line.strip()

        if indent_level == 0:
            formatted_lines.append(last_indent_char + formatted_line)
        else:
            formatted_lines.append(indent_char * (indent_level - 1) + last_indent_char + formatted_line)

    formatted_tree = '\n'.join(formatted_lines)
    print("format_tree: " + formatted_tree)
    return formatted_tree

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the PowerShell script
script_path = os.path.join(current_dir, "powershell_tree_generator.ps1")

# Execute the PowerShell script
subprocess.run(["pwsh-preview", "-File", script_path])

powershell_output = subprocess.run(['pwsh-preview', '-File', './my_first_script.ps1'], capture_output=True, text=True).stdout

done = False

formatted_tree = format_tree(powershell_output)

# the command to execute in PowerShell is an array of strings
command = [
    "pwsh-preview", # this is the PowerShell executable command
    "-Command", # this tells PowerShell that the next string will be the command to execute
    r'$formatted_tree = """' + formatted_tree + '"""\n', # here we define a variable in PowerShell called $formatted_tree and assign it the value of the formatted tree
    "$formatted_tree" # this is the command to print the value of the $formatted_tree variable
]

# Execute PowerShell command
# Here the run method is used instead of the check_output method because the check_output method will raise an exception if the PowerShell command returns a non-zero exit code
# so the run method is called on the subprocess object instead and the output is captured in the stdout attribute to be used later bound to the output variable
output = subprocess.run(command, capture_output=True, text=True, input=powershell_output).stdout

# Create a markdown file with the formatted tree
# with tells Python to open the file and close it when the block ends, open tells Python to open the file in write mode, and the "w" argument tells Python to open the file in write mode
with open("TREE.md", "w") as f:
    f.write(formatted_tree) # write the formatted tree to the file

# Print PowerShell output
print(output)

```

</details>

This Python script generates a directory tree structure by utilizing the PowerShell script mentioned above. The `format_tree` function formats the tree structure, and the remaining code executes the PowerShell script, captures the output, takes user input for the directory tree structure, formats the tree, executes PowerShell commands, creates a markdown file with the formatted tree, and prints the PowerShell output.

## Downloads

You will need to download and install the following software to run the scripts:

PowerShell: This script was tested with PowerShell 7.1.3, but it should work with PowerShell 5.1 as well. Download it on a [PC](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell) or [MAC](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-macos).

## Installation

Please follow these steps to run the script:

1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Navigate to the project directory: `cd directory-tree-generator`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the script: `python powershell_tree_generator.py`
3. Follow the on-screen instructions to provide the directory tree structure.
4. Once completed, a file named "tree.md" will be generated with the file tree structure.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

