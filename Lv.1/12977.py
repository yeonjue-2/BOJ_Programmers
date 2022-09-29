def solution(nums):
    answer = 0

    for i in nums:
        for j in nums[nums.index(i)+1:]:
            for k in nums[nums.index(j)+1:]:
                number = i + j + k

                cnt = 0
                for m in range(1, int(number ** 0.5) + 1):
                    if number % m == 0:
                        cnt += 1

                if cnt == 1:
                    answer += 1


    return answer
  

