n = int(input())
family_tree = {}

for _ in range(n):
    pair = input().split()
    if pair[0] not in family_tree:
        family_tree[pair[0]] = [pair[1]]
    else:
        family_tree[pair[0]].append(pair[1])


def counter(tree, parent):
    if parent not in tree:
        return 0

    children = len(tree[parent])
    for child in tree[parent]:
        children += counter(tree, child)
    return children


person = input()
print(counter(family_tree, person))
