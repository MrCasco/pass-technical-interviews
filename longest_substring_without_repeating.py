"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
"""

def longest_substring_without_repeating_characters(string: str) -> int:
    if not string:
        return 0
    seen = {}
    left, right = 0, 0
    mx = 1
    while right < len(string):
        if string[right] in seen:
            mx = max(mx, len(string[left:right]))
            while string[left] != string[right]:
                seen.pop(string[left])
                left += 1
            left += 1
            seen[string[left]] = left
        else:
            seen[string[right]] = right
            mx = max(mx, len(string[left:right+1]))
        right += 1
    return mx

print(longest_substring_without_repeating_characters('abccabcabcc'))
print(longest_substring_without_repeating_characters('abcdbea'))
print(longest_substring_without_repeating_characters('aaaaabaaaa'))
