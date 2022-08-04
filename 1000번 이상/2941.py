

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for w in croatia:
    word = word.replace(w, "*")
print(len(word))

# 위에 해당 하는 단어가 word에 있을 경우 *로 바꿈
# word = ljes=njak -> *e**ak  -> 총 길이 = 6
