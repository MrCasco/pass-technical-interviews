def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns):
        return False
    a_b = {}
    b_a = {}
    for a, b in zip(strings, patterns):
        if a_b.get(a) == None:
            if b_a.get(b) != None:
                return False
            a_b[a] = b
            b_a[b] = a
        elif a_b.get(a) != b:
            return False
    return True

def areFollowingPatterns2(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))

print(areFollowingPatterns(['cat', 'dog', 'doggy'], ["a", "b", "b"]))
print(areFollowingPatterns2(['cat', 'dog', 'doggy'], ["a", "b", "b"]))
