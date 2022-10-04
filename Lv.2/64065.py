def solution(s):
    answer = []
    s = s[:-2].replace('{', '').replace(',', ' ').split('}')

    for i, v in enumerate(s):
        s[i] = v.split()

    n = len(s)

    for i in range(1, n+1):
        for k in s:
            if len(k) == i:
                for j in k:
                    if j not in answer:
                        answer.append(j)

    answer = [int(i) for i in answer]

    return answer
  
  
 
# 리팩토링 코드
def solution(s):
    answer = []
    s = s[:-2].replace('{', '').replace(',', ' ').split('}')   # 문자열에서 필요없는 것들 제거

    s = [i.split() for i in s]        # 나눠서 리스트 형태로 만듦

    s.sort(key=len)                   # 리스트의 길이가 작은 것부터 정렬

    for i in s:
        for j in i:                   # 리스트의 원소가 answer에 없으면 int형태로 append
            if int(j) not in answer:
                answer.append(int(j))

    return answer

  
  
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# -> [2, 1, 3, 4]

