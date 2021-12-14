import sys

sys.path.insert(1, 'C:\Python\check-if-want-to-pass-technical-interviews')

def text_reader():
    f = open("C:\Python\check-if-want-to-pass-technical-interviews\inputs/day_6/lanternfish.txt", "r")
    return [int(num) for num in f.readline().split(',')]

def get_children(initial, n):
    if initial >= n:
        return 0
    return 1 + (n//7 if initial == 6 else (n-initial-1)//7)

def get_all_descendants(initial, days):
    if (initial, days) in memo:
        return memo[(initial, days)]
    if initial >= days:
        return 1
    children = 0
    for i in range(get_children(initial, days)):
        children += get_all_descendants(8, days-((7*i)+initial+1))
    memo[(initial, days)] = children + 1
    return 1 + children

def lanternfish_simulation(initial, days):
    fishes = 0
    for num in initial:
        if (num, days) not in memo:
            memo[(num, days)] = get_all_descendants(num, days)
        fishes += memo[(num, days)]
    return fishes

# Tests
initial_state = [1, 1, 6]
initial_state = [3, 4, 3, 1, 2]
initial_state = [1]

memo = {}
initial_state = text_reader()

# PART 1
days = 80
print(lanternfish_simulation(initial_state, days))

# PART 2
days = 256
print(lanternfish_simulation(initial_state, days))


"""
3 4 3 1 2     day 0
2 3 2 0 1
1 2 1 6 0 8
0 1 0 5 6 7 8
6 0 6 4 5 6 7 8 8
5 6 5 3 4 5 6 7 7 8    day 5
4 5 4 2 3 4 5 6 6 7
3 4 3 1 2 3 4 5 5 6
2 3 2 0 1 2 3 4 4 5
1 2 1 6 0 1 2 3 3 4 8
0 1 0 5 6 0 1 2 2 3 7 8   day 10
6 0 6 4 5 6 0 1 1 2 6 7 8 8 8
5 6 5 3 4 5 6 0 0 1 5 6 7 7 7 8 8
4 5 4 2 3 4 5 6 6 0 4 5 6 6 6 7 7 8 8
3 4 3 1 2 3 4 5 5 6 3 4 5 5 5 6 6 7 7 8
2 3 2 0 1 2 3 4 4 5 2 3 4 4 4 5 5 6 6 7  day 15
1 2 1 6 0 1 2 3 3 4 1 2 3 3 3 4 4 5 5 6 8
0 1 0 5 6 0 1 2 2 3 0 1 2 2 2 3 3 4 4 5 7 8
6 0 6 4 5 6 0 1 1 2 6 0 1 1 1 2 2 3 3 4 6 7 8 8 8 8   day 18   26 children

1
0
6 8
5 7
4 6
3 5
2 4
1 3
0 2
6 1 8
5 0 7        day 10
4 6 6 8
3 5 5 7
2 4 4 6
1 3 3 5
0 2 2 4       day 15
6 1 1 3 8
5 0 0 2 7
4 6 6 1 6 8 8
3 5 5 0 5 7 7
2 4 4 6 4 6 6 8
1 3 3 5 3 5 5 7      day 21   8 children
0 2 2 4 2 4 4 6
6 1 1 3 1 3 3 5 8
5 0 0 2 0 2 2 4 7
4 6 6 1 6 1 1 3 6 8 8 8    day 25
3 5 5 0 5 0 0 2 5 7 7 7
2 4 4 6 4 6 6 1 4 6 6 6 8 8 8
1 3 3 5 3 5 5 0 3 5 5 5 7 7 7
0 2 2 4 2 4 4 6 2 4 4 4 6 6 6 8   day 29
6 1 1 3 1 3 3 5 1 3 3 3 5 5 5 7 8  17 children
5 0 0 2 0 2 2 4 0 2 2 2 4 4 4 6 7
4 6 6 1 6 1 1 3 6 1 1 1 3 3 3 5 6 8 8 8 8
3 5 5 0 5 0 0 2 5 0 0 0 2 2 2 4 5 7 7 7 7
2 4 4 6 4 6 6 1 4 6 6 6 1 1 1 3 4 6 6 6 6 8 8 8 8 8 8   27 children
1 3 3 5 3 5 5 0 3 5 5 5 0 0 0 2 3 5 5 5 5 7 7 7 7 7 7   day 35
0 2 2 4 2 4 4 6 2 4 4 4 6 6 6 1 2 4 4 4 4 6 6 6 6 6 6 8 8 8 8  31 children

0  1 1 6
1  0 0 5
2  6 6 4 8 8
3  5 5 3 7 7
4  4 4 2 6 6
5  3 3 1 5 5
6  2 2 0 4 4
7  1 1 6 3 3 8
8  0 0 5 2 2 7
9  6 6 4 1 1 6 8 8
10 5 5 3 0 0 5 7 7
11 4 4 2 6 6 4 6 6 8 8
12 3 3 1 5 5 3 5 5 7 7
13 2 2 0 4 4 2 4 4 6 6
14 1 1 6 3 3 1 3 3 5 5 8
15 0 0 5 2 2 0 2 2 4 4 7
16 6 6 4 1 1 6 1 1 3 3 6 8 8 8
17 5 5 3 0 0 5 0 0 2 2 5 7 7 7
18 4 4 2 6 6 4 6 6 1 1 4 6 6 6 8 8 8 8
19 3 3 1 5 5 3 5 5 0 0 3 5 5 5 7 7 7 7
20 2 2 0 4 4 2 4 4 6 6 2 4 4 4 6 6 6 6 8 8
21 1 1 6 3 3 1 3 3 5 5 1 3 3 3 5 5 5 5 7 7 8      21 children

0  8 8 8
1  7 7 7
2  6 6 6
3  5 5 5
4  4 4 4
5  3 3 3
6  2 2 2
7  1 1 1
8  0 0 0
9  6 6 6 8 8 8
10 5 5 5 7 7 7
11 4 4 4 6 6 6
12 3 3 3 5 5 5
13 2 2 2 4 4 4
14 1 1 1 3 3 3
15 0 0 0 2 2 2
16 6 6 6 1 1 1 8 8 8
17 5 5 5 0 0 0 7 7 7
18 4 4 4 6 6 6 6 6 6 8 8 8
19 3 3 3 5 5 5 5 5 5 7 7 7
20 2 2 2 4 4 4 4 4 4 6 6 6
21 1 1 1 3 3 3 3 3 3 5 5 5
22 0 0 0 2 2 2 2 2 2 4 4 4
23 6 6 6 1 1 1 1 1 1 3 3 3 8 8 8
24 5 5 5 0 0 0 0 0 0 2 2 2 7 7 7
25 4 4 4 6 6 6 6 6 6 1 1 1 6 6 6 8 8 8 8 8 8
26 3 3 3 5 5 5 5 5 5 0 0 0 5 5 5 7 7 7 7 7 7
"""
