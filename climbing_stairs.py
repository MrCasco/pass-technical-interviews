def climbing_stairs(steps, stairs):
    staircase = [1] + [0 for _ in range(stairs)]
    total_ways = {}
    for i in range(1, stairs+1):
        number_ways = 0
        total_ways[i] = []
        for step in steps:
            if i-step >= 0:
                total_ways[i].append(i-step)
                number_ways += staircase[i-step]
                staircase[i] = number_ways
    return number_ways, total_ways

stairs = int(input('How many steps are there on the staircase? '))
steps = [1, 2, 3]
num_ways, total_ways = climbing_stairs(steps, stairs)
print('There are', num_ways, 'different ways to climb', stairs, 'steps with these steps', steps)
print('Here are the whole ways you can climb:', total_ways)
