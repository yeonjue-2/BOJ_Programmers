from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))   # 신고 결과를 중복 없이
    user = defaultdict(set)      # 유저별 신고한 id 저장, 중복 안되게 set
    cnt = defaultdict(int)       # 신고 당한 횟수

    for r in report:
        a,b = r.split()
        user[a].add(b)
        cnt[b] += 1             # key의 값이 기본적으로 int 0이 되어있기 때문에 바로 +1 가능

    for id in id_list:          # muzi : {neo, frodo}  2번 신고함
        result = 0
        for u in user[id]:      # neo           # frodo
            print(u)
            if cnt[u] >= k:     # cnt[neo] = 2  # 2
                print(cnt[u])
                result += 1
        answer.append(result)   # 1 추가         # 1추가    -> 2추가
    return answer


print(solution(["muzi"], ["muzi frodo"], 2))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))


# -> [0]
#   [2, 1, 1, 2]
#   무, 프, 어,     




