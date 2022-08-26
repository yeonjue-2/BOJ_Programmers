def recs(s, f, N, ff, M):
    global blue, white
    cnt = 0
    cnt_1 = 0
    for i in range(f, N):            # 첫번째 범위
        for j in range(ff, M):       # 두번째 범위
            if s[i][j] == 0:
                cnt += 1
            else:
                cnt_1 += 1
    if cnt == (N - f) ** 2:          # 0과 1의 개수가 전체와 같다면
        white += 1
    elif cnt_1 == (N - f) ** 2:
        blue += 1
    else:                            # 아니라면 재귀
        recs(s, f, (N+f)//2, ff, (M+ff)//2)      # 2사분면    2 | 1    
        recs(s, f, (N+f)//2, (M+ff)//2, M)       # 1사분면    3 | 4
        recs(s, (N+f)//2, N, ff, (M+ff)//2)      # 3사분면
        recs(s, (N+f)//2, N, (M+ff)//2, M)       # 4사분면


N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]  # 행렬 채우기
blue = 0
white = 0

recs(s, 0, N, 0, N)
print(white)
print(blue)
