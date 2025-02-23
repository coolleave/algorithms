n, k = list(map(int, input().split()))
lst = list(map(int, input().split()))

lst.sort()
lst_reverse = sorted(lst, reverse=True)
left = 0
right = n - 1


# 是否能打包成mid个花束
def check(mid):
    # 打包花束需要的总花朵数量
    count = 0

    # 每个追求者能贡献的花朵数量，最多贡献mid朵
    for i in range(n):
        count += min(mid, lst[i])
    return count >= mid * k


# 二分
res = 0
while left <= right:
    mid = (left + right) // 2
    # 能够打成mid个花束
    if check(mid):
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
