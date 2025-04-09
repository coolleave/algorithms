n = int(input())
lst = list(map(int, input().split()))
# 构造列表 自循环
fa = list(i for i in range(100001))


def find(x):
    if x != fa[x]:
        fa[x] = find(fa[x])
    return fa[x]


for i in range(n):

    lst[i] = find(lst[i])
    # 最关键的部分，将父亲变成 lst[i] + 1的父亲
    fa[lst[i]] = find(lst[i]+1)
s = " ".join(map(str, lst))
print(s)
