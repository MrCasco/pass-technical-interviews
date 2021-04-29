## FIRST VARIANT ##
def slowest_key(keys):
    ALPHABET = dict(zip([_ for _ in range(27)], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    last_time = 0
    slowest = ('', 0)
    for key, time in keys:
        if time-last_time > slowest[1]:
            slowest = (ALPHABET[key], time-last_time)
        last_time = time
    return slowest[0]

## LEETCODE VARIANT ##
def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    if not releaseTimes or not keysPressed:
        return None
    last_time = 0
    slowest = ('1', 0)
    for key, time in zip(keysPressed, releaseTimes):
        if time-last_time > slowest[1]:
            slowest = (key, time-last_time)
        elif time-last_time == slowest[1]:
            next_key = sorted([key, slowest[0]])
            slowest = (next_key[1], time-last_time)
        last_time = time
    return slowest[0]

print(slowest_key([(0, 1), (3, 4), (0, 8), (2, 11)]))
print(slowest_key([(0, 1), (3, 4), (0, 8), (2, 11)]))
