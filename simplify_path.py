def simplifyPath(path: str) -> str:
    path = path.split('/')
    i = 0
    file = ''
    while i < len(path):
        if path[i] == '' or path[i] == '.':
            pass
        elif path[i] == '..':
            if '/' in file:
                file = file[:file.rindex('/')]
        else:
            file += '/'+path[i]
        i += 1
    if file == '':
        return '/'
    return file


"/home/"
"/../"
"/home//foo/"
"/a/./b/../../c/"
