from collections import deque

# 读取矩阵大小n m
n, m = map(int, input().split())
# 初始化一个空矩阵
matrix = []
x0, y0, d = (0, 0, 0)
for x in range(n):
    row = []
    string = input()
    for char in string:
        # 找出起始s的坐标
        if char == 'S':
            x0, y0 = x, string.index('S')
        row.append(char)
    matrix.append(row)

# 方向8个
directions = [(-1, 2), (1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

# 创建队列,坐标和豆子数为0
queue = deque([(x0, y0)])
# 使用列表推导式 标记走过的位置
visiabled = [[False] * m for _ in range(n)]
visiabled[x0][y0] = True
while queue:
    # 取出坐标和豆子数
    x, y = queue.popleft()
    # 四个方向扩散
    for direction in directions:
        dx, dy = x + direction[0], y + direction[1]
        # 条件筛选
        if 0 <= dx < n and 0 <= dy < m and matrix[dx][dy] != 'S' \
                and matrix[dx][dy] != 'x' and visiabled[dx][dy] == False:
            # 符合条件 标记
            visiabled[dx][dy] = True
            #  豆子数
            if matrix[dx][dy] == 'b':
                d = d + 1
            queue.append((dx, dy))

print(d)
