n = int(input())
lst = list(map(int, (input().split())))
sum = [0] * n
sum[0] = lst[0]
# 求前缀和
for i in range(1, n):
    sum[i] = sum[i - 1] + lst[i]

ans = 10 ** 18
# 从0，p次任务放到gpu1  p+1 ， n-1 到 gpu2 的时间
for p in range(1, n):
    temp_time = max(sum[p - 1], sum[n - 1] - sum[p-1])
    ans = min(ans, temp_time)

print(ans)
