n = int(input())
n = str(n)

if n[-1] == "0" or n[-1] == "1" or n[-1] == "6" or n[-1] == "8":
    print("pon")
elif n[-1] == "3":
    print("bon")
else:
    print("hon")