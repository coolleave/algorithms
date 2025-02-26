# 认为success为胜利的一方，其他两方为失败
def procced(inf, success, fail1, fail2):
    # 方案的数量
    nas = 0
    # 兵力差  success - fail1 - fail2
    amy = 0
    fail_method = []
    for sechme in inf:
        total = sechme[success] - sechme[fail1] - sechme[fail2]
        # 如果单个方案够，将剩下的人员作为富余兵力
        if total > 0:
            # 兵力积攒
            amy += total
            # 方案加1
            nas += 1
        else:
            # 如果单个方案无法达到要求，就加入失败方案列表，让富余兵力进行平账
            fail_method.append(total)
    # 对失败方案进行排序，因为是复数，要按着从大到小的顺序排列，贪心算法
    fail_method.sort(reverse=True)
    for method in fail_method:
        # 富余不够再加此失败方案了 直接返回
        if amy + method <= 0:
            break
            # 富余能够平账此失败方案，方案数加一
        else:
            amy = amy+method
            nas += 1
    # 如果一个满足要求的方案都没有，直接返回-1
    if nas == 0:
        return -1
    return nas


n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
inf = []
# 将数据添加到inf中
for i in range(n):
    inf.append([a[i], b[i], c[i]])

# 最大方案数为
max_number = max(
    procced(inf, 0, 1, 2),
    procced(inf, 1, 0, 2),
    procced(inf, 2, 1, 0)
)

print(max_number)
