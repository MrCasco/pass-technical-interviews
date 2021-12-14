def text_reader(file):
    f = open("C:\Python\check-if-want-to-pass-technical-interviews\inputs/"+file, "r")
    res = []
    for line in f:
        res.append(line.strip('\n'))
    return res
