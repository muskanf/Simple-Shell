# Simple-Shell
A shell is the command console (terminal) that you can use to navigate your computer (such as "terminal" on a Mac, "PowerShell" on Windows, or "ssh" when you connect to the CS department linux machines). The underlying operating system on a MacBook is a Unix-like operating system.
Sure, here's a first-person description of the text:

# My Terminal Program Project

In this assignment, I wrote a simple terminal program (also known as a shell). A shell is the command console used to navigate a computer. I created a "fake" file system and my commands interacted with that file system.

## Shell Operations
- `cd <name of directory>`: Change directory. Move to new directory. `..` is the parent directory.
- `ls`: List all files and folders in current directory.
- `touch <filename>`: Make new empty file with given name.
- `mkdir <directory name>`: Make new empty directory with given name.
- `pwd`: Output path to current directory, starting with root.
- `rm <filename>`: Remove file. Error if used on directory name.
- `rmdir <directory name>`: Remove EMPTY directory. Error if used on file or non-empty directory.
- `tree`: Pretty-print contents of directory recursively using pre-order traversal with current directory as root.

## What I Implemented
- I wrote a `FileSystem` class to store the tree and a `TreeNode` class.
- The `FileSystem` class contains information about existing folders/files and has methods for various commands.
- In main, I read user input from keyboard and called appropriate methods.

### TreeNode class
- Instance variables:
  - `name` of type String
  - `children` of type list of TreeNode objects (None if not a directory)
  - `parent` of type TreeNode
  - `is_directory` of type boolean
- `__init__()` takes in name, parent node, and value for is_directory.
- `append_child(name, is_directory)`: add new child to node
- `is_root()`: return true if node is root
- `__str__()`: returns string representation of TreeNode

### FileSystem
- Instance variables:
  - `root` of type TreeNode
  - `current_directory` of type TreeNode
- `__init__()`: makes root TreeNode with empty string for name and sets current directory to newly made root node.
- `check_make_file(name)`: If current directory has child with name already, raises ValueError. Otherwise do nothing.
- `ls()`: Prints all children of current directory.
- `mkdir(dirname)`: Adds new directory child node to current directory. Raises ValueError if name already exists.
- `touch(name)`: Same as mkdir but makes new file, not directory.
- `cd(name)`: Changes current_directory to name. If current_directory doesn't have child with given name that is a directory, raise ValueError.
