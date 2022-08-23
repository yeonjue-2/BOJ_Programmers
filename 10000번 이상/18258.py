import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    M = sys.stdin.readline().split()

    if M[0] == 'push':
        queue.append(M[1])
    elif M[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif M[0] == 'size':
        print(len(queue))
    elif M[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif M[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
