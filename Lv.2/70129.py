def solution(s):
    a, b = 0, 0

    while int(s) > 1:
        b += s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))[2:]
        a += 1

    return [a, b]
