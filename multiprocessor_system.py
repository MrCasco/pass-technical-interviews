from heapq import heapify, heappop, heappush

## NAIVE SOLUTION WITH N^2 ##
def multiprocessor_system(workers, tasks):
    return multiprocessor_system_handler(workers, tasks, 0)

def multiprocessor_system_handler(workers, tasks, steps):
    if tasks <= 0:
        return steps
    task = max(workers)
    workers[workers.index(task)] = workers[workers.index(task)]//2
    return multiprocessor_system_handler(workers, tasks-task, steps+1)

## BEST SOLUTION USING A HEAP ##
def multiprocessor_system(workers, tasks):
    workers = [-x for x in workers]
    heapify(workers)
    hours = 0
    while tasks > 0:
        cur_task = -heappop(workers)
        tasks -= cur_task
        heappush(workers, -(cur_task//2))
        hours += 1
    return hours

print(multiprocessor_system([3, 1, 7, 2, 4], 15))
print(multiprocessor_system([4, 2, 8, 3, 5], 19))
print(multiprocessor_system([10, 6], 20))
