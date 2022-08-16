a, b = map(int, input().split())
a_list = list(map(int, input().split()))

cur_min = 1
cur_max = max(a_list)

while cur_min <= cur_max:
    avg = (cur_min + cur_max) // 2
    tree = 0
    for i in a_list:
        if i >= avg:
            tree += i - avg
    if tree >= b:
        cur_min = avg + 1
    else:
        cur_max = avg - 1

print(cur_max)



# 1. min, max 값을 지정한다.
# 2. min, max 값이 같아질 때까지 자르고 남은 나무의 길이를 구한다.
# 3. 구한 값이 target number = b 보다 크면 min += 1 (빼주는 값을 키워야 함)
#    b보다 작으면 max -= 1
