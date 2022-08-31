N = int(input())
answer = []
cnt = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if 100001*i + 10001*j + 1001*k + 101*l + 11*m + 2*n == N:
                            cons = i*100000+ j*10000 + k*1000 + l*100 + m*10 + n
                            answer.append(cons)
                            cnt += 1
                        else:
                            cnt += 0

if cnt != 0:
    print(answer[0])
else:
    print(0)
    
    
    
N = int(input())
result = 0

for i in range(1, N+1):
    M = list(map(int, str(i)))
    result = i + sum(M)
    if result == N:
        print(i)
        break

    if i == N:
        print(0)
