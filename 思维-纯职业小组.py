# t组数据
t = int(input())
lst = []
for _ in range(t):
    # 小队的数量和组成的纯职业小组的数量
    n, k = tuple(map(int, input().split()))
    # 小队的职业和数量
    dic = {}
    for i in range(n):
        a, b = tuple(map(int, input().split()))
        # 如果a存在，原值加b，如果不存在 赋值为0  加b
        dic[a] = dic.get(a, 0) + b
    total = 0
    for item in dic:
        total += item // 3
    if total>=k:
        lst.append(1)

print(lst)