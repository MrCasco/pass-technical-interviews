"""
A company has n employees with a unique ID for each employee from 0 to n - 1.
The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct
manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination
relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news.
He will inform his direct subordinates, and they will inform their subordinates, and so on until all
employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates
(i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

Example 1:
    Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    Output: 1
    Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
    The tree structure of the employees in the company is shown.

Example 2:
    Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
    Output: 21
    Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
    The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
    The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
    The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
    The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
    The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
    Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.
"""

from collections import defaultdict
def numOfMinutes(n, headID, manager, informTime):
    subs = defaultdict(list)
    for sub, boss in enumerate(manager):
        if boss != -1:
            subs[boss] += [sub]
    time = float('-inf')
    queue = [(headID, headID, 0)]
    cur_boss = headID
    while queue:
        boss, lboss, cur_time = queue.pop(0)
        if cur_boss != lboss:
            time = max(time, cur_time)
            cur_boss = lboss
        if boss in subs:
            for sub in subs[boss]:
                queue.append((sub, boss, cur_time+informTime[boss]))
    return max(time, informTime[headID])

print(numOfMinutes(10, 3, [8,9,8,-1,7,1,2,0,3,0], [224,943,160,909,0,0,0,643,867,722]))
print(numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2, 1]))
print(numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
