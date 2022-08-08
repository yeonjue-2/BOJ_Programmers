N = int(input())    
div = N
div_list = []

while div > 0:
    M = map(int, input().split())          
    for i in M:
        div_list.append(i)
        div -= 1

div_list.sort()

if N == 1:
    print(div_list[0] * div_list[0])
else:
    print(div_list[0] * div_list[-1])
    
    
    
# 간략하게 list 사용

N = int(input())    # 4
M = list(map(int, input().split()))
M.sort()

if N == 1:
    print(M[0] ** 2)
else:
    print(M[0] * M[-1])
