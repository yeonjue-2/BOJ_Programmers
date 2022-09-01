A = list(map(str, input()))
B = list(map(str, input()))
cnt = 0

if sorted(A) == sorted(B):        # 정렬 후 비교
    boo = True
else:
    boo = False


for i in range(len(A) - 1, -1, -1):   
    if A[i] == B[len(A) - 1 - cnt]:       # 순서가 다른 개수만큼 이동 필요
        cnt += 1

print(len(A) - cnt) if boo else print(-1)
