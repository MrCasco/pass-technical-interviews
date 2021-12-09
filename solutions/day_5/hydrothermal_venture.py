import sys
from collections import defaultdict

sys.path.insert(1, 'C:\Python\check-if-want-to-pass-technical-interviews')

def text_reader():
    f = open("C:\Python\check-if-want-to-pass-technical-interviews\inputs/day_5/hydrothermal_venture.txt", "r")
    coords = []
    for line in f:
        a, b = line.split(' -> ')
        first = tuple(int(num) for num in a.split(','))
        second = tuple(int(num) for num in b.split(','))
        coords.append((first, second))
    return coords

def hydrothermal_venture():
    coords = text_reader()
    dots = defaultdict(lambda: 0)
    dangerous_dots = 0
    for left, right in coords:
        x1, y1 = left
        x2, y2 = right
        diff = 0
        begin = 0
        if x1 != x2 and y1 != y2: continue
        if x1 == x2:
            begin = min(y1, y2)
            diff = max(y1, y2) - begin
        else:
            begin = min(x1, x2)
            diff = max(x1, x2) - begin
        for i in range(diff+1):
            if x1 == x2:
                dots[(x1, begin+i)] += 1
                if dots[(x1, begin+i)] == 2:
                    dangerous_dots += 1
            else:
                dots[(begin+i, y1)] += 1
                if dots[(begin+i, y1)] == 2:
                    dangerous_dots += 1
    return dangerous_dots

def diagonal_hydrothermal_venture():
    coords = text_reader()
    dots = defaultdict(lambda: 0)
    dangerous_dots = 0
    for left, right in coords:
        x1, y1 = left
        x2, y2 = right
        diff = 0
        begin = 0
        if x1 == x2 or y1 == y2:
            begin = min(y1, y2) if x1 == x2 else min(x1, x2)
            diff = (max(y1, y2) if x1 == x2 else max(x1, x2)) - begin
            for i in range(diff+1):
                if x1 == x2:
                    dots[(x1, begin+i)] += 1
                    if dots[(x1, begin+i)] == 2:
                        dangerous_dots += 1
                else:
                    dots[(begin+i, y1)] += 1
                    if dots[(begin+i, y1)] == 2:
                        dangerous_dots += 1
        else:
            dx = -1 if x1-x2 > 0 else 1
            dy = -1 if y1-y2 > 0 else 1
            for i in range(abs(x1-x2)+1):
                dots[(x1+(i*dx), y1+(i*dy))] += 1
                if dots[(x1+(i*dx), y1+(i*dy))] == 2:
                    dangerous_dots += 1
    return dangerous_dots

# PART 1
print(hydrothermal_venture())

# PART 2
print(diagonal_hydrothermal_venture())
