def solution(dartResult):

    dartResult = dartResult.replace('10', 'k')
    arr = ['10' if i == 'k' else i for i in dartResult]
    answer = []

    i = -1                  # index 주의
    sdt = ['S', 'D', 'T']

    for j in arr:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j) + 1)
        elif j == '*':
            answer[i] *= 2
            if i >= 1:
                answer[i-1] *= 2
        elif j == '#':
            answer[i] *= -1
        else:
            answer.append(int(j))           # 숫자가 들어갔을 때 index 증가
            i += 1

    return sum(answer)
