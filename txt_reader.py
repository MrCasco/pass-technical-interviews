def text_reader(file):
    f = open("./inputs/"+file, "r")
    res = []
    for line in f:
        res.append(line.strip('\n'))
    return res
