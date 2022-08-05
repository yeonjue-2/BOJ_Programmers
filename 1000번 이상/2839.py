

N = int(input())

bag = 0
while N >= 0:
    if N%5 == 0:      # 5의 배수이면 바로 프린트 후 종료
        bag += N//5
        print(bag)
        break

    N -= 3            # 아니라면 3씩 빼서 5의 배수가 되는지
    bag +=1

else:
    print(-1)
    
    
