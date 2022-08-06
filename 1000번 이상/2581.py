

import math

N = int(input())
M = int(input())
prime_list = []

# 1. i가 나눠떨어진다면 제외
# 2. 나눠 떨어지지 않는다면 m += 1
# 3. 그래도 안되면 prime_list에 추가
# 4. list에 하나도 추가되지 않았다면 -1 반환

for i in range(N, M + 1):           
    i_sqrt = int(math.sqrt(i))
    if i > 1:
        for m in range(2, i_sqrt + 1):            
            if i % m == 0:              
                break
            else:
                continue
        else:
            prime_list.append(i)            


if len(prime_list) > 0:
    print(sum(prime_list))
    print(prime_list)
    print(min(prime_list))
else:
    print(-1)
    
    
