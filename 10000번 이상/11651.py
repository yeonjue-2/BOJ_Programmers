

N = int(input())
a_list = []

for i in range(N):
    a = list(map(int, input().split()))
    a_list.append([a[1], a[0]])

a_list.sort()
for i in a_list:
    print(i[1], i[0])
    
    
