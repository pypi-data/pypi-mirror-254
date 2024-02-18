import os

def touch_file(path : str, content :str = None):
    """
    Open a file at the specified path and write the content if provided. 
    :param path: str - the path to the file
    :param content: str - the content to be written to the file (optional)
    """
    f = open(path, 'a')
    if content:
        f.write(content)
    f.close()
    
def get_files(path : str, *types):
    """
    Returns a list of files with the specified types in the given directory.

    :param path: A string representing the directory path.
    :param types: Variable number of string arguments representing file types.
    :return: A list of files with the specified types.
    """
    if len(types) == 0:
        return []
    
    files = []
    for file in os.listdir(path):
        if any([file.endswith(t) for t in types]):
            files.append(file)
        
    return files