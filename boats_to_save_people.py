def boats_to_save_people(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    boats = 0
    while left <= right:
        if left == right:
            boats += 1
            break
        if people[left]+people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats

print(boats_to_save_people([1, 2, 2], 5))
print(boats_to_save_people([1, 2], 3))
print(boats_to_save_people([3, 5, 3, 4], 5))
