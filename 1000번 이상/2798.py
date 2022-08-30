N, M = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for i in range(N):
	for j in range(i+1, N):
        for k in range(j+1, N):
        	if card[i] + card[j] + card[k] > M:
            	continue   # M보다 큰 값은 제외
            else:
            	result = max(result, card[i] + card[j] + card[k])

print(result)
