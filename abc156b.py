a = list(map(int,input().split()))

#コピペ
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

print(len(Base_10_to_n(a[0], a[1])))