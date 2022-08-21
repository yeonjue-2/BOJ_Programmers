# 1. cnt < n 일 때까지 while문을 돌려 stack에 push (cnt += 1)
# 2. stack[-1] == n 이면 pop, result에 부호 넣어줌
# 3. 아니라면 result에 NO 반환


N = int(input())
cnt = 0
stack = []  # 넣었다 뺄 stack
result = []

for i in range(0, N):
    n = int(input())

    while cnt < n:
        cnt += 1
        stack.append(cnt)
        result.append("+")

    if stack[-1] == n:
        stack.pop()
        result.append("-")

    else:
        result.clear()
        print("NO")
        break

for i in result:   		# ->   print("\n".join(result))
    print(i)
