def main():
    s = input()
    ans = "Yes"
    for i, st in enumerate(s):
        if i % 2 == 0:
            if st.isupper():
                ans = "No"
        else:
            if st.islower():
                ans = "No"
    print(ans)

if __name__ == '__main__':
    main()