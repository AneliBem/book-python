from array import array
from collections import deque
import bisect
from heapq import heapify, heappop, heappush

a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])


d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('Handling', d.popleft())


def breadth_first_search(unsearched):
    unsearched = deque([starting_node])
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)


scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)


data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
print([heappop(data) for i in range(3)])