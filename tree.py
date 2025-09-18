import os
import argparse


def print_sub_tree(filePath, directory, depth, max_depth):
    try:
        full_path = os.path.join(filePath, directory)
        print("    " * depth + "|-- " + directory + "/")
        # Stop recursion if max_depth is reached
        if depth >= max_depth:
            return depth
        sub_dirs = [d for d in os.listdir(full_path) if os.path.isdir(os.path.join(full_path, d))]
        return print_dirs_to_tree(full_path, sub_dirs, depth + 1, max_depth)
    except PermissionError:
        print("  " * depth + "|-- " + directory + " [Permission Denied]")
        return depth
    except Exception as e:
        print("  " * depth + "|-- " + directory + f" [Error: {str(e)}]")
        return depth

"""
Description: Print directories to tree 
Params: 
    filePath         -> str: either ~ or current working directory 
    dirs             -> list of str: populated with all directories of filePath 
    depth            -> int: default 0 
    max_depth        -> int: command line argument for max depth of subtrees 
"""
def print_dirs_to_tree(filePath, dirs, depth, max_depth):
    max_depth_reached = depth
    for directory in dirs:
        local_depth = print_sub_tree(filePath, directory, depth, max_depth)
        if local_depth > max_depth_reached:
            max_depth_reached = local_depth
    return max_depth_reached

"""
Description: return filepath based on args 
Params: 
    args -> command line args 
"""
def get_filepath(args):
    if args.root:
        return os.path.expanduser("~")
    else: 
        return os.getcwd()

def exclude_dotfiles_from_list(exclude_dotfiles, dirs):
    if exclude_dotfiles: 
        return [d for d in dirs if not d.startswith('.')]
    return dirs

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Print working directory tree")
    parser.add_argument('--exclude-dotfiles', action='store_true', help="Exclude dotfiles (files/directories starting with '.')")
    parser.add_argument('--max-depth', type=int, default=float('inf'), help="Maximum depth to traverse (default: unlimited)")
    parser.add_argument('--root', action='store_true', help="Run tree from root instead of current working directory")
    args = parser.parse_args()

    filePath = get_filepath(args)

    try:
        dirs = [d for d in os.listdir(filePath) if os.path.isdir(os.path.join(filePath, d))] # all dirs in filepath pre filtering 
        dirs = exclude_dotfiles_from_list(args.exclude_dotfiles, dirs) # filter out dotfiles based on argument 

        print_dirs_to_tree(filePath, dirs, 0, args.max_depth) 

    except Exception as e:
        print(f"Error accessing {filePath}: {str(e)}")

if __name__ == "__main__":
    main()