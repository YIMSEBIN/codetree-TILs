n = int(input())
words = []
for _ in range(n) :
    words.append(input())

words.sort()

for i in range(n) :
    print(words[i])