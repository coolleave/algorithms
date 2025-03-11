# 判断是否能到 mid 点
def check(mid, n):
    # 计算海嗣到达所需的时间
    time_list = [(mid - h_list[i][0]) // h_list[i][1] for i in range(n)]
    # time_list = [(mid - h_list[i][0]) // h_list[i][1] for i in range(n)]
    # 排序
    time_list.sort()
    # 判断每只海嗣是否超过
    for second in range(n):
        # 第 second 秒 能否通过 小于则在击杀之前就到达。
        if time_list[second] < second:
            return False
    return True


# 接收数据
# 海嗣
n = int(input())
# 海嗣的起点和每秒的移动速度
h_list = []
for _ in range(n):
    (d, v) = list(map(int, input().split()))
    h_list.append((d, v))
# 二分
left = 0
right = 10 ** 18
mid = 0
while left <= right:
    mid = (left + right) // 2
    # 符合条件，尝试更小的
    if check(mid, n):
        right = mid - 1
    else:
        left = mid + 1

print(left)
