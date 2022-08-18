# Q. 두 수의 최소공배수 구하기
# math 이용

import sys
import math
N = int(sys.stdin.readline())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))
    
    
    
# 식 만들어 계산
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    gcd = 1
    for j in range(1, a + 1):
        if a % j == 0 and b % j == 0:
            gcd = j
    print(a * b // gcd)
    
    # 최대 공약수를 구하여 두 수의 곱을 나눈다

