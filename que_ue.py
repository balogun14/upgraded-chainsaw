from collections import deque


que_ue = deque()
que_ue.append(1)
que_ue.append(2)
que_ue.append(3)
que_ue.append(4)

print(que_ue)
x = que_ue.popleft()
print(x)
print(que_ue)
