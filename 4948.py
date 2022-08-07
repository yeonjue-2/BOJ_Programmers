# 첫번째 풀이(시간초과)

import math

while True:
    N = int(input())
    cnt = 0

    if N == 0:
        break

    for i in range(N + 1, (2*N + 1)):
        i_sqrt = int(math.sqrt(i))
        if i > 1:
            for m in range(2, i_sqrt + 1):
                if i % m == 0:
                    break
                else:
                    continue
            else:
                cnt += 1
    print(cnt)
    

# 두번째 풀이(에리스토테네스의 체 사용)

while True:
    N = int(input())  
    
    if N == 0:				# 0에 대한 처리도 적절한 곳에 해주어야 함
        break

    prime_list = [True for _ in range(N * 2 + 1)]
    prime_list[0], prime_list[1] = False, False			# 0,1
    cnt = 0

    m = int((2 * N) ** 0.5)  
    for i in range(2, m + 1):  
        if prime_list[i]:
            for j in range(i + i, N * 2 + 1, i):  
                prime_list[j] = False			# 체를 이용하여 판별해놓고

    for i in range(N + 1, (2 * N + 1)):  
        if prime_list[i]:
            cnt += 1
    print(cnt)

    
