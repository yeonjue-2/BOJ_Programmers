import numpy as np

def solution(numbers, hand):
    answer = []

    for i in numbers:
        index = np.where(s == i)

        if i == 1 or i == 4 or i == 7:                    # 반드시 L
            answer.append("L")
            cur_L.clear()
            cur_L.append([int(index[0]), int(index[1])])

        elif i == 3 or i == 6 or i == 9:                  # 반드시 R
            answer.append("R")
            cur_R.clear()
            cur_R.append([int(index[0]), int(index[1])])
        else:                                             # 그 외
            re_L = abs(index[0] - cur_L[0][0]) + abs(index[1] - cur_L[0][1])
            re_R = abs(index[0] - cur_R[0][0]) + abs(index[1] - cur_R[0][1])
            if re_L > re_R:                                     # 오른쪽에서 거리가 더 가까울 경우
                answer.append("R")
                cur_R.clear()
                cur_R.append([int(index[0]), int(index[1])])
            elif re_R > re_L:                                   # 왼쪽에서 거리가 더 가까울 경우
                answer.append("L")
                cur_L.clear()
                cur_L.append([int(index[0]), int(index[1])])
            else:                                               # 거리가 같은 경우
                if hand == "right":
                    answer.append("R")
                    cur_R.clear()
                    cur_R.append([int(index[0]), int(index[1])])
                else:
                    answer.append("L")
                    cur_L.clear()
                    cur_L.append([int(index[0]), int(index[1])])



    return ''.join(answer)


s = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 0, 12]])
cur_L = [[3,0]]
cur_R = [[3,2]]
