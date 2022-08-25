import collections
import sys

N = int(sys.stdin.readline())
arr = []

if N % 2 == 1:                          # 홀수인 경우에만
    for i in range(N):
        M = int(sys.stdin.readline())
        arr.append(M)

arr.sort()                              # 숫자들을 arr에 넣고 sort

count_list = collections.Counter(arr).most_common()  # Counter를 사용해 각각의 개수를 dict 형태로 받고
max = count_list[0][1]                               # most_common(n)을 사용해 최빈값 n개를 리스트에 담긴 튜플형태로 반환
                                                     # 가장 많이 나온 횟수를 max로 저장
count_list_1 = []                                    # 최빈값의 순서대로 나온 key들을 저장할 리스트

for i in range(len(count_list)):                     # key들만 저장
    value = count_list[i][1]
    count_list_1.append(value)

if count_list_1.count(max) != 1:                     # 최빈값이 여러개일 경우 최빈값 중 두 번째로 작은 값을 출력
    count_max = count_list[1][0]
else:
    count_max = count_list[0][0]

ss = round(sum(arr) / N)                 # 값을 반올림
center = arr[N // 2]
range = arr[-1] - arr[0]


print(ss)
print(center)
print(count_max)
print(range)
