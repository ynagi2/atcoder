k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    print("{}...".format(s[:k]))