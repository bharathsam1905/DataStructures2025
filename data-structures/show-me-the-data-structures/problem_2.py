import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    list_files=[]
    if not os.path.isdir(path):
        return [] 
    else:
        for each_item in (os.listdir(path)):
            full_path=os.path.join(path,each_item)
            clean_path = os.path.normpath(full_path).replace("\\", "/")
            if os.path.isfile(full_path) and full_path.endswith(suffix):
                list_files.append(clean_path)
            elif os.path.isdir(clean_path):
                list_files.extend(find_files(suffix,clean_path))
                
    return list_files
   
        
if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./data-structures/show-me-the-data-structures/testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

# Test Case 2: Directory contains no .c files
    print("\nTest Case 2: Directory contains no .c files")
    result = find_files(".c", "./data-structures/show-me-the-data-structures/emptydir")
    print(result)  # Expected: []

    # Test Case 3: Invalid path
    print("\nTest Case 3: Invalid directory path")
    result = find_files(".c", "./invalid/path")
    print(result)  # Expected: []