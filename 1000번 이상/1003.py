# 1  -> 시간초과 (일일이 다 구하기)
def fibo(n, dict):
    global cnt_0, cnt_1
    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    else:
        return fibo(n-1, dict) + fibo(n-2, dict)


N = int(input())

for i in range(N):
    M = int(input())
    dict = {}
    cnt_0 = 0
    cnt_1 = 0
    fibo(M, dict)
    print(str(cnt_0) + " " +str(cnt_1))

    
    
# 2 -> 성공(memoization 사용)
def fibo(n, dict):
    if n == 0:
        dict[0] = [1, 0]
        return dict[0]
    elif n == 1:
        dict[1] = [0, 1]
        return dict[1]
    elif len(dict) >= n:
        return dict[n]        # 바로 사용
    else:
        f = fibo(n-1, dict)[0] + fibo(n-2, dict)[0]
        b = fibo(n-1, dict)[1] + fibo(n-2, dict)[1]
        dict[n] = [f, b]
        return dict[n]


N = int(input())

for i in range(N):
    M = int(input())
    dict = {}           # -> 3 일 경우 {1: [0, 1], 0: [1, 0], 2: [1, 1], 3: [1, 2]}
    print(fibo(M, dict)[0], fibo(M, dict)[1])  
    
    
    
    
# 3 -> 2번과 시간은 똑같은데 더욱 간결해 보임, 
#      0의 갯수 = 이전 1의 갯수, 1의 갯수 = 이전 0+이전1 갯수
t = int(input())
 
for _ in range(t):
    cnt_0 = [1,0]     # 0이 나온 횟수
    cnt_1 = [0,1]     # 1이 나온 횟수
    n = int(input())
    if n>1:
        for i in range(n-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2]+cnt_1[-1]) 
 
    print(cnt_0[n], cnt_1[n])
  
  
  
