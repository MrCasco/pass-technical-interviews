import sys
sys.path.insert(1, 'C:\Python\check-if-want-to-pass-technical-interviews')


def text_reader(file):
    f = open("C:\Python\check-if-want-to-pass-technical-interviews\inputs/"+file, "r")
    return [int(num) for num in f.readline().strip('\n').split(',')]

def board_reader():
    f = open("C:\Python\check-if-want-to-pass-technical-interviews\inputs/day_4/bingo.txt", "r")
    f.readline()
    f.readline()
    boards = []
    cur_board = {'rows': [0 for _ in range(5)], 'cols': [0 for _ in range(5)]}
    row = 0
    for line in f:
        if line == '\n':
            row = 0
            boards.append(cur_board)
            cur_board = {'rows': [0 for _ in range(5)], 'cols': [0 for _ in range(5)]}
            continue
        line = line.split()
        for col in range(len(line)):
            num = int(line[col])
            cur_board[num] = (row, col)
        row += 1
    return boards

def sum_not_checked(board):
    board.pop('rows')
    board.pop('cols')
    return sum(board.keys())

def get_winner_board():
    bingo_nums = text_reader('day_4/bingo.txt')
    boards = board_reader()
    last_board = {}
    last_num = 0
    for num in bingo_nums:
        for i, board in enumerate(boards):
            if num in board:
                row, col = board[num]
                board['rows'][row] += 1
                board['cols'][col] += 1
                board.pop(num)
                if board['rows'][row] == 5 or board['cols'][col] == 5:
                    last_board = board
                    last_num = num
                    boards.pop(i)
    return last_board, last_num

board, last_num = get_winner_board()
print(sum_not_checked(board) * last_num)
