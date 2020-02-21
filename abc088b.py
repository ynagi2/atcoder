n = int(input())
card = list(map(int,input().split()))

card.sort(reverse=True)
alice = []
bob = []

for i in range(len(card)):
    if i % 2 == 0:
        alice.append(card[i])
    else:
        bob.append(card[i])

print(sum(alice)-sum(bob))