def bracket_match(text):
    stack = []
    count = 0
    for bracket in text:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                count += 1
            else:
                stack.pop()
    return count+len(stack)

print(bracket_match('(((('))
print(bracket_match('((((())))'))
print(bracket_match(')('))
print(bracket_match('((()()(())()()()))'))
