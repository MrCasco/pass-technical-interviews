"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
"""

def convert(self, s: str, rows: int) -> str:
    if rows == 1 or rows == len(s): return s
    res = ['']*rows
    cur_row = 1
    mul = -1
    for i in range(len(s)):
        cur_row += mul
        res[cur_row] += s[i]
        if cur_row == rows-1 or cur_row == 0:
            mul *= -1
    return ''.join(res)
