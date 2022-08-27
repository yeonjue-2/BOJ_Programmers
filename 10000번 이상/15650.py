N, M = map(int, input().split())
s = []

def back(start):
    if len(s) == M:                     # 길이가 M이면 출력
        print(' '.join(map(str, s)))

    for i in range(start, N+1):
        if i not in s:              # i가 리스트에 없으면 추가
            s.append(i)             # 재귀 실행
            back(i+1)
            s.pop()


back(1)
