"""
Here is some info on Unix file system paths:

    / is the root directory; the path should always start with it even if it isn't there in the given path;
    / is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;
        this also means that // stands for "change the current directory to the current directory"
    . is used to mark the current directory;
    .. is used to mark the parent directory; if the current directory is root already, .. does nothing


Example:

For path = "/home/a/./x/../b//c/", the output should be
simplifyPath(path) = "/home/a/b/c"
"""

def simplifyPath(path):
    new_path = []
    path = path.strip('/').split('/')
    for dire in path:
        if dire == '.' or dire == '':
            continue
        elif dire == '..':
            if not new_path:
                continue
            new_path.pop()
        else:
            new_path.append(dire)
    return '/'+'/'.join(new_path)
