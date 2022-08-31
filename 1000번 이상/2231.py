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
    
    

#
N = input()
a = int(N)-9*len(N)   # 88 - 18 = 70
if a < 0:
    a = 0

N = int(N)
b = False

while not b and a < N:
    s = a
    for i in range(len(str(a))):    # 0, 1
        s += int(str(a)[i])         # 70+7+0 = 77, 71+7+1 = 79, ... 80+8 = 88
    if N == s:
        print(a)
        b = True
    a += 1                          # a = 71       72       73  ... 80
if b == False:
    print(0)
