def solution(sizes):
    h = 1
    w = 1

    for i in range(len(sizes)):
        sizes[i].sort()
        if h <= sizes[i][0]:
            h = sizes[i][0]

        if w <= sizes[i][1]:
            w = sizes[i][1]

    answer = h * w

    return answer
