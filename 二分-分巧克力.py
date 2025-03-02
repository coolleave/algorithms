n, k = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
# print(lst)

left = 1
right = 10 ** 5


# 能否切开
def check(mid):
    total = 0
    for item in lst:
        h = item[0]
        w = item[1]
        if h // mid > 0 and w // mid > 0:
            total += (h // mid) * (w // mid)
            # print(total)
        if total >= k:
            # print("yes",mid)
            return True
    return False


mid = 0
# 二分
while left <= right:

    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(left - 1)
