word = input().upper()            # Apple -> APPLE
word_list = list(set(word))       # 중복된 문자 제거 ['L', 'A', 'E', 'P']

cnt = []
for char in word_list:
  cnt.append(word.count(char))    # 원래 단어에서 개수를 세어 저장  [1, 1, 1, 2]
    
if cnt.count(max(cnt)) > 1:       # 가장 큰 수의 개수가 하나 이상일 때
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])     # cnt.index(2)   2라는 값을 가지고 있는 배열의 index 값
            P           3        2
