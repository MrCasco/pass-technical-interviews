import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:\Python\check-if-want-to-pass-technical-interviews')

from txt_reader import text_reader

def report_repair(arr):
    arr = {key: i for i, key in enumerate(arr)}
    for num in arr:
        if 2020-num in arr:
            return (2020-num) * num



arr = [int(num) for num in text_reader('day_1/report_repair.txt')]
print(report_repair(arr))
