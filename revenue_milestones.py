def getMilestoneDays(revenues, milestones):
    milestones = sorted([(milestone, i) for i, milestone  in enumerate(milestones)])
    cur = 0
    days = 0
    total_revenue = 0
    res = [-1]*len(milestones)
    for revenue in revenues:
        total_revenue += revenue
        days += 1
        if cur < len(milestones):
            while cur < len(milestones) and total_revenue >= milestones[cur][0]:
                index = milestones[cur][1]
                res[index] = days
                cur += 1
        else:
            break
    return res

print(getMilestoneDays([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 200, 500]))
print(getMilestoneDays([100, 200, 300, 400, 500], [300, 800, 1000, 1400]))
print(getMilestoneDays([700, 800, 600, 400, 600, 700], [3100, 2200, 800, 2100, 1000]))
print(getMilestoneDays([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 2000, 5]))
