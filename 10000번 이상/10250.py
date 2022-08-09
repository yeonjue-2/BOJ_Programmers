N = int(input())

while N > 0:
    a, b, c = map(int, input().split())    

    Y = str(c % a)                           
    X = str((c // a) + 1)            

    if c % a == 0:            # 딱 나누어 떨어질 때, 6층까지인데 12번째 손님
        Y = str(a)            # 6층
        X = str(c // a)       # 12 // 6 = 2, 2호실

    if len(X) == 1:
        X = ('0' + X)
    print(Y + X)
    N -= 1
