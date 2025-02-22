# 判断区域是否合理
# x区域长度 regions 区域列表 n 所需的区域个数
def isRegion(x, regisons, n):
    # totalRegion 已经划分的区域个数
    total_region = 0
    for region in regisons:
        # 计算区间
        total_region += region // x
        # 总数量已经够了
        if total_region >= n:
            return True
    return total_region >= n


# 二分查找
def find_max(left, right):
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if isRegion(mid, regions, n):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


# 数据接收
n, m = map(int, input().split())
regions = list(map(int, input().split()))
left = 1
right = max(regions)
print(find_max(left, right))
