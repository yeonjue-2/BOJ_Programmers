

N = int(input())
sixs = 666
cnt = 0

while True:
    if '666' in str(sixs):    # 666, 1666, 2666, ...
        cnt += 1

    if cnt == N:
        print(sixs)
        break

    sixs += 1                 # 666, 667, 668, ... 하나씩 늘려나가다가 666이 포함되면 cnt += 1
    
    
