

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    distance = b - a				        # 11
    n = 0
    
    while True:
        if distance <= n * (n+1):	  # 11 < 3*4, n = 3 
            break
        n += 1												
        													
    if distance <= n ** 2:							
        print(n * 2 - 1)									
        													
    else:							              # 11 > 9 = 3 ** 2	 
        print(n * 2)
        
        
