n = int(input())
a = [int(input()) for _ in range(n)]

paper = set()

for elem in a:
    if elem in paper:
        paper.discard(elem)
    else:
        paper.add(elem)

print(len(paper))
