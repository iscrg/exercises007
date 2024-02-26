n = int(input())

antonyms = {}

for _ in range(n):
    antonym = input().split()
    antonyms[antonym[0]] = antonym[1]

word = input()
if word in antonyms.keys():
    print(antonyms[word])
else:
    print(word)
