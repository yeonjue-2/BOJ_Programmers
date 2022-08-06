import sys

N = int(sys.stdin.readline())
m = 2

while N != 1:
    if N % m == 0:
        print(m)
        N //= m
    else:
        m += 1
        
# Q.정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.        
# ->  처음엔 소수를 받아놓고 하나씩 꺼내려고 했음(오륲)        

