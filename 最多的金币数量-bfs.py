"""

小蓝为了寻宝来到了一个迷宫，这个迷宫是一个
n
×
m
n×m 的矩阵，矩阵元素由
0
0 和
1
1 构成，小蓝现在需要从起点走到终点，他只能 上下左右移动且走值为
1
1 ** 的格子。当他走到终点时，他可以 **获得矩阵中值为
0
0 的格子的数量的金币。现在小蓝可以使用一个魔法，该魔法只能使用 一次，魔法的功能为在他 开始出发前 可以将 **任意个值为
1
1 的格子变成
0
0**，现在问你小蓝在走到终点后能获得的最大金币为多少？

数据保证在一开始时，有一条起点通往终点的路线，你无法将起点与终点变成
0
0。

输入格式
第一行输入二个整数
n
,
m
n,m，代表矩阵大小。

第二行输入四个整数
x
1
,
y
1
,
x
2
,
y
2
x
1
​
 ,y
1
​
 ,x
2
​
 ,y
2
​
 ，代表起点与终点坐标。

接下来
n
n 行每行输入一个长度为
m
m 的 01 串，代表迷宫的构造情况。

输出格式
输出小蓝能获得的最大金币数量。
"""

from collections import deque


# 进行搜索
def bfs_search(x1, y1, x2, y2):
    step = 0
    # 判重
    visiabled = set()
    queue = deque([(x1, y1, step)])
    visiabled.add((x1, y1))
    # 方向
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x0, y0, step = queue.popleft()
        if (x0, y0) == (x2, y2):
            print(n * m - step - 1)
        for direction in directions:
            dx = x0 + direction[0]
            dy = y0 + direction[1]
            if 0 <= dx < n and 0 <= dy < m and lst[dx][dy] == '1' and (dx, dy) not in visiabled:
                queue.append((dx, dy, step + 1))
                visiabled.add((dx, dy))


if __name__ == '__main__':
    # 接收数据
    n, m = list(map(int, input().split()))
    # 起始终止位置
    x1, y1, x2, y2 = list(map(int, input().split()))

    lst = []
    for _ in range(n):
        lst.append(list(input()))
    # 带入参数并处理坐标
    bfs_search(x1 - 1, y1 - 1, x2 - 1, y2 - 1)
