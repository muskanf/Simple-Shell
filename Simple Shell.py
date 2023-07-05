
import pickle

class TreeNode:
    def __init__(self, name, parent, is_directory):
        # Initialize a new TreeNode object with the given name, parent, and is_directory flag
        self.name = name
        self.parent = parent
        self.is_directory = is_directory
        # If this node is a directory, initialize its children as an empty list; otherwise, set its children to None
        self.children = [] if is_directory else None

    def append_child(self, name, is_directory):
        # Add a new child to this node with the given name and is_directory flag
        if self.is_directory:
            # If this node is a directory, create a new TreeNode object for the child and add it to the children list
            new_child = TreeNode(name, self, is_directory)
            self.children.append(new_child)
        else:
            # If this node is not a directory (i.e., it is a file), print an error message
            print("Cannot add child to a file")

    def is_root(self):
        # Return True if this node has no parent (i.e., it is the root of the tree), and False otherwise
        return self.parent is None

    def __str__(self):
        # Return a string representation of this node
        if self.is_directory:
            # If this node is a directory, include the <directory> tag in its string representation
            return f"{self.name} <directory>"
        else:
            # If this node is not a directory (i.e., it is a file), just return its name
            return self.name



class FileSystem:
    def __init__(self):
        # Initialize a new FileSystem object with a root TreeNode object that represents the root directory
        self.root = TreeNode("", None, True)
        # Set the current directory to the root directory
        self.current_directory = self.root

    def check_make_file(self, name):
        # Check if a file or directory with the given name already exists in the current directory
        for child in self.current_directory.children:
            if child.name == name:
                # If a file or directory with the given name already exists, raise a ValueError
                raise ValueError(f"{name} already exists")

    def ls(self):
        # List the contents of the current directory
        for child in self.current_directory.children:
            print(child.name)

    def mkdir(self, dirname):
        # Create a new directory with the given name in the current directory
        # First, check if a file or directory with the given name already exists
        self.check_make_file(dirname)
        # If no file or directory with the given name exists, create a new directory by appending a new child TreeNode object to the current directory
        self.current_directory.append_child(dirname, True)

    def touch(self, name):
        # Create a new file with the given name in the current directory
        # First, check if a file or directory with the given name already exists
        self.check_make_file(name)
        # If no file or directory with the given name exists, create a new file by appending a new child TreeNode object to the current directory
        self.current_directory.append_child(name, False)

    def cd(self, name):
        # Change the current directory to the specified directory
        if name == "..":
            # If the specified directory is "..", move up one level in the directory tree by setting the current directory to its parent
            if not self.current_directory.is_root():
                self.current_directory = self.current_directory.parent
            else:
                # If the current directory is already the root directory, raise a ValueError because we cannot go above the root directory
                raise ValueError("Cannot go above root directory")
        else:
            # If the specified directory is not "..", search for a child TreeNode object in the current directory that has the same name and is a directory
            for child in self.current_directory.children:
                if child.name == name and child.is_directory:
                    # If such a child TreeNode object is found, set it as the new current directory and return
                    self.current_directory = child
                    return
            # If no such child TreeNode object is found, raise a ValueError because the specified directory does not exist
            raise ValueError(f"{name} is not a valid directory")

    def rm(self, filename):
        # Remove the specified file from the current directory
        for i, child in enumerate(self.current_directory.children):
            if child.name == filename and not child.is_directory:
                # If a child TreeNode object with the same name as the specified file is found and it is not a directory (i.e., it is a file), remove it from the children list of the current directory and return
                del self.current_directory.children[i]
                return
        # If no such child TreeNode object is found, raise a ValueError because the specified file does not exist
        raise ValueError(f"{filename} is not a valid file")

    def rmdir(self, dirname):
        # Remove the specified empty directory from the current directory
        for i, child in enumerate(self.current_directory.children):
            if child.name == dirname and child.is_directory:
                if len(child.children) == 0:
                    # If a child TreeNode object with the same name as the specified directory is found and it is an empty directory (i.e., it has no children), remove it from the children list of the current directory and return
                    del self.current_directory.children[i]
                    return
                else:
                    # If such a child TreeNode object is found but it is not empty (i.e., it has children), raise a ValueError because we cannot remove non-empty directories
                    raise ValueError(f"{dirname} is not empty")
        # If no such child TreeNode object is found, raise a ValueError because the specified directory does not exist
        raise ValueError(f"{dirname} is not a valid directory")

    def tree_helper(self, node, level):
        # Helper function to recursively print all nodes in subtree rooted at node at depth level in tree format
        print("\t" * level + str(node))
        if node.children is not None:
            for child in node.children:
                self.tree_helper(child, level + 1)

    def tree(self):
        # Print all nodes in subtree rooted at current_directory in tree format by calling tree_helper function on current_directory at depth 0
        self.tree_helper(self.current_directory, 0)

    def pwd_helper(self, node):
        # Helper function to recursively build path of node by concatenating names of all ancestor nodes separated by "/"
        if node.is_root():
            return "/"
        else:
            return self.pwd_helper(node.parent) + node.name + "/"

    def pwd(self):
        # Print path of current_directory by calling pwd_helper function on current_directory
        print(self.pwd_helper(self.current_directory))

    def user_input(self):
        while True:
            text = input('').split()
            if text[0] == 'quit':
                break
            try:
                if text[0] == 'ls':
                    self.ls()
                elif text[0] == 'pwd':
                    self.pwd()
                elif text[0] == 'tree':
                    self.tree()
                elif text[0] == 'cd':
                    name = text[1]
                    self.cd(name)
                elif text[0] == 'mkdir':
                    name = text[1]
                    self.mkdir(name)
                elif text[0] == 'touch':
                    name = text[1]
                    self.touch(name)
                elif text[0] == 'rm':
                    name = text[1]
                    self.rm(name)
                elif text[0] == 'rmdir':
                    name = text[1]
                    self.rmdir(name)
            except Exception as e:
                print(e)



def test_filesystem(fs):
    fs.tree()
    fs.touch('first_file')
    fs.tree()
    fs.mkdir('testing_folder')
    fs.tree()
    fs.rmdir('testing_folder')
    fs.tree()
    fs.mkdir('testing_folder')
    fs.tree()
    fs.cd('testing_folder')
    fs.tree()
    fs.mkdir('testing_folder2')
    fs.tree()
    fs.cd('testing_folder2')
    fs.tree()
    fs.cd('..')
    fs.cd('..')
    fs.touch('testing_again')
    fs.rm('testing_again')


def _main():
 file_system = FileSystem()

 # Call the test_filesystem function to test that everything works
 test_filesystem(file_system)

 # Call the user_input function to take all the user inputs and operate like a normal shell
 file_system.user_input()


def _main_with_pickle():
    try:
        with open("file_system.bin", "rb") as file_source:
            file_system = pickle.load(file_source)
        print("File System loaded")
    except:
        print("Creating a new file system: file doesn't exist or data file is out of date because FileSystem class changed")
        file_system = FileSystem()

 # Call the test_filesystem function to test that everything works
    test_filesystem(file_system)

 # Call the user_input function to take all the user inputs and operate like a normal shell
    file_system.user_input()

    with open("file_system.bin", "wb") as file_destination:
        pickle.dump(file_system, file_destination)
    print("File system saved")


if __name__=='__main__':
 _main_with_pickle()

