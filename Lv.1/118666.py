def solution(survey, choices):
    answer = []
    type = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    type_num = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(survey)):
        if choices[i] < 4:
            index = type.index(survey[i][0])
            type_num[index] += 4 - choices[i]
        elif choices[i] > 4:
            index = type.index(survey[i][1])
            type_num[index] += choices[i] - 4

    for i in range(0, 8, 2):
        if type_num[i] < type_num[i + 1]:
            answer.append(type[i + 1])
        else:
            answer.append(type[i])

    answer = "".join(answer)
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))

# TCMA
# RCJA
