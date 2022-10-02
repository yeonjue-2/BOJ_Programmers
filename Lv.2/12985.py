def solution(n,a,b):
    answer = 0

    while a / 2 != b / 2:
        if a % 2 == 0 and b % 2 == 0:
            a = a//2
            b = b//2
        elif a % 2 == 0 and b % 2 != 0:
            a = a//2
            b = (b+1)//2
        elif a % 2 != 0 and b % 2 == 0:
            a = (a+1) // 2
            b = b // 2
        else:
            a = (a + 1) // 2
            b = (b + 1) // 2
        answer += 1


    return answer
  
  
  

def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
