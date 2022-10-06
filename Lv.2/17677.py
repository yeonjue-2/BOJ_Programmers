import re

def solution(str1, str2):

    str1 = str1.lower()			# 소문자로 변경
    str2 = str2.lower()

    list_1 = []					# 두 글자씩으로 담을 리스트
    list_2 = []

    same = []					# 교집합 리스트

    for i in range(len(str1) - 1):
        str = str1[i] + str1[i+1]

        if re.match("[a-z]", str[0]) and re.match("[a-z]", str[1]):
            list_1.append(str)

    for i in range(len(str2) - 1):
        str = str2[i] + str2[i+1]

        if re.match("[a-z]", str[0]) and re.match("[a-z]", str[1]):
            list_2.append(str)


    for i in list_1:
        for j in list_2:
            if i == j:
                same.append(i)
                list_2.remove(j)
                break

    for i in list_1:
            list_2.append(i)


    if list_2:
        answer = int((len(same) / len(list_2)) * 65536)
    else:
        answer = 65536

    return answer
    
    
    
# 개선된 남의 풀이
def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)  # 중복된 원소를 제거한 합집합
    res1 = [] 		# 교집합
    res2 = [] 		# 합집합

    if tlist:
        for i in tlist:
            res1.extend([i]*min(list1.count(i), list2.count(i)))  # 가장 작은 횟수의 개수만큼 리스트에 추가
            res2.extend([i]*max(list1.count(i), list2.count(i)))  # 가장 많은 횟수의 개수만큼 리스트에 추가

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536
