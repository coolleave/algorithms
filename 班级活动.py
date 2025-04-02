n = int(input())
a = list(map(int, input().split()))

da = {}
# 出现次数为1
flag1 = 0
# 出现次数为2或以上
flag2 = 0

# 设置字典
for i in a:
    da[i] = da.get(i, 0) + 1

for i, j in da.items():
    if j == 1:
        flag1 += 1
    if j > 2:
        flag2 += j - 2

if flag2 > flag1:
    print(flag2)
else:
    print(flag2 + (flag1 - flag2) // 2)
