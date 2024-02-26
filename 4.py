n = int(input())
attributes = {}

for _ in range(n):
    line = input().split()
    attributes[line[0]] = line[1:]

word = input()

for attribute in attributes:
    if word in attributes[attribute]:
        print(attribute)
        break
