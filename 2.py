n = int(input())
translations = {}

for _ in range(n):
    word = input().split()
    translations[word[0]] = word[1]

sentence = input().split()

for word in sentence:
    if word in translations.keys():
        word_index = sentence.index(word)
        sentence[word_index] = translations[word]

print(' '.join(sentence))
