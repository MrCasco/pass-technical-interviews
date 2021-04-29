from collections import deque
from string import ascii_letters
from typing import List

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    words = set(word_list) # make a set because existence query is O(1) vs O(N) for list
    queue = deque([begin])
    distance = 0
    while len(queue) > 0:
        n = len(queue)
        distance += 1
        for _ in range(n):
            word = queue.popleft()
            for i in range(len(word)):
                for c in ascii_letters:
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word not in words:
                        continue
                    if next_word == end:
                        return distance
                    queue.append(next_word)
                    words.remove(next_word) # removing from the set is equivalent as marking the word visited
    return 0

if __name__ == '__main__':
    begin = input()
    end = input()
    word_list = input().split()
    res = word_ladder(begin, end, word_list)
    print(res)
