N = int(input())
check = 0

for i in range(N):
    str = input()
    cnt = 0
    for index in range(len(str) - 1):
        if str[index] != str[index + 1]:  # 연달은 두 문자가 다른 때,
            new_str = str[index + 1:]     # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_str.count(str[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                cnt += 1
    if cnt == 0:
        check += 1
    N -= 1

print(check)



# 최종 더 간결한 풀이!

N = int(input())
cnt = N

for i in range(N):
    str = input()
    for j in range(0, len(str)-1):
        if str[j] == str[j+1]:    # 연속적으로 같은 문자는 ok
            pass
        elif str[j] in str[j+1:]: # 연속적이지 않고, 남은 문자로 만든 문자열에 해당 문자가 있다면
            cnt -= 1
            break

print(cnt)

