"""
1 2 4 6 7 8 9 4 6 8 10 5
操作k次
假设操作 b p次
a 操作的前缀和是 s[n-1] - s[n-1-p]
b 操作的前缀和就是s[2p-1]

"""
n, k = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()
ans = 10 ** 19
sum = [0] * n
sum[0] = lst[0]
# 计算前缀和
for i in range(1, n):
    sum[i] = sum[i - 1] + lst[i]

# 循环
for p in range(k + 1):
    # 判断，取小值
    # p次b操作的和值,k-p 次 a操作
    temp_sum = sum[n - 1] - sum[n - 1 - (k-p)] + sum[2 * p - 1]  # 前边为a操作的和 后边为b操作的和
    ans = min(ans, temp_sum)

print(ans)
