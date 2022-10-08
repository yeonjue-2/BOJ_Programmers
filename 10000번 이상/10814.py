import sys

N = int(sys.stdin.readline())
dict = {}

for i in range(N):
    n, m = sys.stdin.readline().split()
    dict[i, n] = m

dict = sorted(dict.items(), key=lambda item: int(item[0][1]))

for i in range(N):
    print(dict[i][0][1], dict[i][1])
