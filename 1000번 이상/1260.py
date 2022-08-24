def dfs(cur_node):
    print(cur_node, end=' ')
    visit[cur_node] = 1      # 방문 노드 체크

    for i in range(1, N + 1):
        if visit[i] == 0 and s[cur_node][i] == 1:   # 방문한 적 없는 인접 노드 방문
            dfs(i)

def bfs(cur_node):

    queue = [cur_node]

    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        visit[node] = 0     # 방문 노드 체크

        for i in range(1, N + 1):
            if visit[i] == 1 and s[node][i] == 1:   # 방문한 적 없는 인접 노드 방문
                if i not in queue:                  # 같은 수가 들어가지 않도록
                    queue.append(i)


N, M, L = map(int, input().split())
s = [[0] * (N + 1) for i in range(N + 1)]  # 행 열 번호를 사용하기위해 0번째 인덱스 0으로 초기화
visit = [0 for i in range(N + 1)]          # 방문 체크 리스트

for i in range(M):                         # s에 인접노드 체크
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(L)			# 1 2 4 3
print()			
bfs(L)			# 1 2 3 4	


# 4 5 1      				              0  1  2  3  4
# 1 2 	  1 = [2, 3, 4]	    s = [[0, 0, 0, 0, 0],
# 1 3     2 = [4]			        1  [0, 0, 1, 1, 1],
# 1 4  	  3 = [4] 		        2  [0, 1, 0, 0, 1],
# 2 4  			    	            3  [0, 1, 0, 0, 1],
# 3 4 		        	          4  [0, 1, 1, 1, 0]]
