words = input().split()

res = {}

for word in words:
    if word not in res:
        res[word] = 1
    else:
        res[word] += 1

res = list(sorted(res.items(), key=lambda x: x[1]))
res = [x[0] for x in res]
res.reverse()

for word in res:
    print(word)
