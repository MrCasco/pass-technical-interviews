# Add any helper functions you may need here
def swipeBooks(books, students, signs):
    t = books.copy()
    for i, student in enumerate(students):
        signs[student-1] += 1
        books[student-1] = t[i]


def findSignatureCounts(students):
    signs = [0]*len(students)
    books = students.copy()
    swipeBooks(books, students, signs)
    while students != books:
        swipeBooks(books, students, signs)
    return signs

print(findSignatureCounts([1, 2]))
print(findSignatureCounts([2, 1]))
print(findSignatureCounts([3, 1, 2]))
print(findSignatureCounts([4, 3, 2, 1]))
print(findSignatureCounts([1, 2, 3, 4]))
