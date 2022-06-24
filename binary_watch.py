def readBinaryWatch(turnedOn):
    # import ipdb; ipdb.set_trace()
    if turnedOn == 0: return ['0:00']
    if turnedOn > 8: return []
    def dfs(time, on, i, res):
        # import ipdb; ipdb.set_trace()
        if time[0] == time[1] == '1' or time[7] == '1' == time[4] == time[5] == time[6]:
            return
        if on == 0:
            real_time = transform_binary_time(time)
            res.append(real_time)
            return
        if i == 10:
            return
        dfs(time[:], on, i+1, res)
        time[i] = '1'
        dfs(time[:], on-1, i+1, res)
    res = []
    dfs(['0']*10, turnedOn, 0, res)
    return res

def transform_binary_time(time):
    hour = str(int(''.join(time[:4]), 2))
    mins = str(int(''.join(time[4:]), 2))
    if len(mins) == 1:
        mins = '0'+mins
    return hour+':'+mins

print(readBinaryWatch(2))
