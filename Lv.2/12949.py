def solution(arr1, arr2):
    col1 = len(arr1[0])
    col2 = len(arr2[0])
    row1 = len(arr1)
    row2 = len(arr2)

    answer = [[0] * col2 for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            sum = 0
            for k in range(col1):
                sum += arr1[i][k] * arr2[k][j]
            answer[i][j] = sum


    return answer
