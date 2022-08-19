A = int(input())

for i in range(A):
    N, M = map(int,input().split())
    result_1 = 1
    result_2 = 1
    fact_list = []

    for i in range(1, N + 1):
        result_1 *= i

    for u in range(M, 0, -1):
        fact_list.append(u)

    for i in range(N):
        result_2 *= fact_list[i]


    print(result_2 // result_1)

