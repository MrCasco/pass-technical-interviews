def defuse(colors):
    red = lambda i: i == len(colors)-1 or (colors[i+1] != 'yellow')
    black = lambda i: i == len(colors)-1 or (colors[i+1] == 'blue' or colors[i+1] == 'green')
    white = lambda i: i != len(colors)-1 and (colors[i+1] in ['yellow', 'blue', 'black', 'red'])
    blue = lambda i: i != len(colors)-1 and colors[i+1] == 'red'
    yellow = lambda i: i == len(colors)-1 or (colors[i+1] != 'white' and colors[i+1] != 'black')
    green = lambda i: True
    rules = {
        'red':red,
        'black':black,
        'white':white,
        'blue':blue,
        'yellow':yellow,
        'green':green
    }
    for i in range(len(colors)):
        rule = rules[colors[i]]
        if not rule(i):
            return True
    return False

print(defuse(['red', 'green', 'blue', 'yellow', 'white', 'black'] ))
print(defuse(['yellow' ,'red' ,'black' ,'green' ,'green' ]))
print(defuse(['white' ,'blue' ,'yellow' ,'green' ,'red' ]))
print(defuse(['black','blue', 'red', 'white', 'yellow', 'green']))
print(defuse(['white','blue', 'red', 'black', 'green', 'yellow']))
print(defuse(['red', 'green', 'blue', 'yellow', 'white', 'black']))
