s = input()

n = len(s)

h = int((n-1)/2)
t = int((n+3)/2 - 1)

head = s[:h]

tail = s[t:]


if s == s[::-1] and head == head[::-1] and tail == tail[::-1]:
    print("Yes")
else:
    print("No")