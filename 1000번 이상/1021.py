
from collections import deque

N, M = map(int, input().split())
answer = list(map(int, input().split()))
queue = deque()
cnt = 0

for i in range(1, N + 1):       # queue 를 만들어 놓기
    queue.append(i)

for i in range(0, M):
    if queue[0] == answer[i]:		# 첫번째 값과 같으면 바로 popleft
        queue.popleft()
        cnt += 0
    else:
        if queue.index(answer[i]) <= (len(queue) // 2):  # index가 보다 작거나 같으면 
            while queue[0] != answer[i]:
                left = queue.popleft()	               	 # 같아질 때까지 left 진행, cnt +1
                queue.append(left)
                cnt += 1
            if queue[0] == answer[i]:		                 # 같아지면 popleft
                queue.popleft()
        else:
            while queue[0] != answer[i]:
                right = queue.pop()
                queue.appendleft(right)
                cnt += 1
            if queue[0] == answer[i]:
                queue.popleft()

print(cnt)


# 1. 왼쪽으로 한 칸 이동시, popleft 한 값을 append -> left
# 2. 오른쪽으로 한 칸 이동시, pop 한 값을 appendleft  -> right
# 3. 구하려 하는 숫자의 index가 전체 인덱스의 반보다 작거나 같으면 left, 크면 right
# ex) 전체길이 5, 5 // 2 -> 2, [0, 1, 2, 3, 4]
#                                   v
