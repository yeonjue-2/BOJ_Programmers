N = int(input())

for i in range(N):
    a, b, r1, d, e, r2 = list(map(int, input().split()))
    dis = ((d-a) ** 2 + (e-b) ** 2) ** 0.5
    if dis == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) < dis < r1+r2:
        print(2)
    elif dis == r1+r2 or dis == abs(r1-r2):
        print(1)
    else:
        print(0)
