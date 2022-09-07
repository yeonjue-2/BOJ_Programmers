from collections import deque

N, M = map(int, input().split())
q = deque([i for i in range(1, N+1)])
num = []

while len(q) > 0:
    for i in range(0, M - 1):
        q.append(q.popleft())
    num.append(q.popleft())

print("<", end="")
for i in num[:-1]:
    print(i, end=", ")
print(num[-1], end=">")

