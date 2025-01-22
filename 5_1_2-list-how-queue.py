from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue)

print(queue.popleft()) # delete element with list on the left
print(queue.popleft())

print(queue)