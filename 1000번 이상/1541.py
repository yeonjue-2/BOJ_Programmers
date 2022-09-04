N = list(map(str, input().split('-')))   # '-' 기준으로 슬라이싱하여 리스트로 저장
plus = []               # 더할 값
minus = []              # 뺄 값

for i in N[1:]:
    if '+' in i:                            # '+'가 포함되어 있으면,
        M = list(map(int, i.split('+')))    # '+'를 기준으로 슬라이싱하여 M 리스트로 저장
        total = sum(M)
        minus.append(total)
    else:                                   # '+'가 포함되어 있지 않은 int형이면
        minus.append(int(i))

if '+' in N[0]:                             # N[0]에 '+'가 포함되어 있다면 
    L = list(map(int, N[0].split('+')))
    total = sum(L)
    plus.append(total)
else:                                       # N[0]이 int형이면
    plus.append(int(N[0]))


print(sum(plus) - sum(minus))



# 다른 풀이
ls= input().split('-')                  # [55, 50+40]
res=[]
for item in ls:
    tmp=list(map(int, item.split('+')))
    res.append(sum(tmp))                # res = [55, 90]

answer=res[0]
for i in range(1, len(res)):
    answer-=res[i]

print(answer)

