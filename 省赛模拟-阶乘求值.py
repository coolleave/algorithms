"""
给定n,求n!除以1000000007的余数。
其中！表示n的阶乘，值为从1连乘到n的积，即n!=
1×2×3×...×n。

(a×b)mod m=[(a mod m)×(b mod m)] mod m
"""

n = int(input())
j = 1
ans = 0
for i in range(2, n + 1):
    j = j * i
    ans = j % 1000000007
print(ans)
