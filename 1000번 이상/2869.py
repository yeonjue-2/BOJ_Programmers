# 1. 낮에 a만큼 올라간다
# 2. height가 c인지 확인
# 3. 아니라면 height -= b    ->  시간 초과


a, b, c = map(int, input().split())

day = 1
height = 0

while height < c:
    height += a
    if height >= c:
        print(day)
        break
    height -= b
    day += 1


# sys, math 모듈을 활용한다

import sys
import math

a,b,c = map(int, sys.stdin.readline().split())

day = (c - b)/(a - b)
print(math.ceil(day))





