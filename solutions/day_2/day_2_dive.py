import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:\Python\check-if-want-to-pass-technical-interviews')

from txt_reader import text_reader


def dive(arr):
    horizontal = 0
    depth = 0
    for ins in arr:
        move, num = ins.split()
        if move == 'down':
            depth += int(num)
        elif move == 'up':
            depth -= int(num)
        else:
            horizontal += int(num)
    return horizontal*depth

def dive_follow_up(arr):
    horizontal = 0
    depth = 0
    aim = 0
    for ins in arr:
        move, num = ins.split()
        if move == 'down':
            aim += int(num)
        elif move == 'up':
            aim -= int(num)
        else:
            horizontal += int(num)
            depth += aim*int(num)
    return horizontal*depth

arr = text_reader('day_2/submarine_course_follow_up.txt')

# print(dive(arr))
print(dive_follow_up(arr))
