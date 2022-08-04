not_self_number = []
for i in range(10000):
    sum = i
    while i != 0:
        sum += i % 10
        i //= 10
    not_self_number.append(sum)

for i in range(10000):
    if i not in not_self_number:
        print(i)