from collections import deque

n, m = map(int, input().split())
# 起始坐标和结束坐标
sx, sy, tx, ty = map(int, input().split())
# 转化为坐标
sx, sy, tx, ty = sx - 1, sy - 1, tx - 1, ty - 1

# k为怪兽数量
k = int(input())
# 怪物坐标
k_lst = []
for _ in range(k):
    x, y = map(int, input().split())
    k_lst.append((x - 1, y - 1))

# 数据集
data = []
# 判重
visibled = set()
visibled.add((sx, sy))
for _ in range(n):
    for char in input().split():
        data.append(char)

# 步数
step = 0
queue = deque([(sx, sy)])
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
flag = 0
while queue:
    x, y = queue.popleft()
    if (x, y) == (tx, ty):
        flag = 1
        print('YES')
        break
    for direction in directions:
        dx = x + direction[0]
        dy = y + direction[1]

        if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visibled and data[dx][dy] != '#' and (dx, dy) not in k_lst:
            queue.append((dx, dy))
            visibled.add((dx, dy))
if not flag:
    print("NO")
