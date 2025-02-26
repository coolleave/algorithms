"""
给定一个数组
A
i
A
i
​
 ，分别求其每个子段的异或和，并求出它们的和。或者说，对于每组满足
1
≤
L
≤
R
≤
n
1≤L≤R≤n 的
L
L,
R
R，求出数组中第
L
L 至第
R
R 个元素的异或和。然后输出每组
L
L,
R
R 得到的结果加起来的值。
"""
# 60 的得分
n = int(input())
lst = list(map(int, input().split()))

# 求前缀异或和
sum = [0] * n
sum[0] = lst[0]
for i in range(1, n):
    sum[i] = sum[i - 1] ^ lst[i]

# 计算异或和之和
total_sum = 0

for i in range(n):
    for j in range(i, n):
        if i == j:
            total_sum += sum[j]
        total_sum += sum[j] ^ sum[i]
print(total_sum)
