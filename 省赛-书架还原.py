n = int(input())
lst = list(map(int, input().split()))

# 找到置换环的数量
# 一个置换环中，交换次数为  k - 1
# 有x个置换环，就有n-x的最少交换次数
count = 0

visited = [False] * n
# 遍历
for i in range(n):
    if not visited[i]:  # 确保没被遍历过
        j = i
        while not visited[j]:  # 如果没被遍历过
            visited[j] = True
            # 找到它应该在的位置
            j = lst[j] - 1
        count += 1  # 找到了一个环

print(n - count)
