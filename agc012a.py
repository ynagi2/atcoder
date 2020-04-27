N = int(input())
a = list(map(int,input().split()))

sort_a = sorted(a, reverse=True)

strong = 0
for i in range(N):
    strong += sort_a[2*i+1]
    # team = [sort_a[2*i], sort_a[2*i+1], sort_a[-i-1]]
    # team.remove(max(team))
    # strong += max(team)
    # つまりはteamの真ん中の数ってことでは？

print(strong)