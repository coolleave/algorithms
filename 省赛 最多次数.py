s = input()
ans = 0
i = 0
while i < (len(s) - 2):
    s1 = s[i:i + 3]
    # print(s1)
    if sorted(s1) == ['b', 'l', 'q']:
        ans += 1
        i += 3
        # print("ans " + s1)
    else:
        i += 1
print(ans)
