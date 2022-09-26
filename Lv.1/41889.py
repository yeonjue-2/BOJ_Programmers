def solution(N, stages):
    answer = []
    t_player = len(stages)       # 플레이어 수
    cnt = 0                      # 해당 레벨까지 도달한 플레이어 수
    rate = {}                    # 각 레벨과 실패율


    for i in range(1, N + 1):
        if (t_player - cnt) != 0:             # division by zero 오류 뜨지 않게!
            values = (stages.count(i) / (t_player - cnt))
            rate[i] = values
            if i == N:
                cnt += stages.count(N + 1)
            else:
                cnt += stages.count(i)
        else:
            rate[i] = 0

    sorted_rate = sorted(rate.items(), key=lambda item: item[1], reverse=True)

    for i in range(len(rate)):
        answer.append(sorted_rate[i][0])

    return answer
