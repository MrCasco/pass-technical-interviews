"""
Given a string paragraph and a string array of the banned words banned, return the most frequent
word that is not banned. It is guaranteed there is at least one word that is not banned, and that
the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.


Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""


from collections import defaultdict
import re

def most_common_word(paragraph, banned):
    words_seen = defaultdict(lambda: 0)
    banned = set(banned)
    most_common = ''
    mx = 0
    normalized = re.sub(r'\W+', ' ', paragraph.lower()).split()
    for word in normalized:
        if word not in banned and word != '':
            words_seen[word] += 1
            if mx < words_seen[word]:
                mx = words_seen[word]
                most_common = word
    return most_common

print(most_common_word('Bob. hIt, ball', ['bob', 'hit']))
print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit."), ["hit"])
print(most_common_word("a.", []))
