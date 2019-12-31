fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append('grape')
print(fruits)
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting a position 4
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
fruits_copy = fruits.copy()
print("copied list of fruits:", fruits_copy)
fruits.clear()
print(fruits)

print()
print("=== Using Lists as Queues ===")

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
queue.append("Grahnam")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


print('\n' * 2)
print("=== List Comprehensions ===")
# List Comprehensions provide a concise way to create lists
squares = []
for x in range(10):
    squares.append(x**2)

print("squares:", squares)

squares_2 = list(map(lambda x: x**2, range(10)))
squares_3 = [x**2 for x in range(10)] 
print("Lambda equivalnet:", squares_2)
print("List comprehension:", squares_3)


print('\n' * 2)
print("=== Another List Comprehnesions Examples ===")
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
print("combs:", combs)

combs_2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print("combs_copy:", combs_2)


print('\n'*2)
print("=== Nested List Comprehensions ===")
# Create a 3x4 matrix: 3 rows and 4 columns
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)

matrix_2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix_2)