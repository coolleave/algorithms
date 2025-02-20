"""
深度搜索bfs
走迷宫

题目描述
给定一个
N
×
M
N×M 的网格迷宫
G
G。
G
G 的每个格子要么是道路，要么是障碍物（道路用
1
1 表示，障碍物用
0
0 表示）。

已知迷宫的入口位置为
(
x
1
,
y
1
)
(x
1
​
 ,y
1
​
 )，出口位置为
(
x
2
,
y
2
)
(x
2
​
 ,y
2
​
 )。问从入口走到出口，最少要走多少个格子。

输入描述
输入第
1
1 行包含两个正整数
N
,
M
N,M，分别表示迷宫的大小。

接下来输入一个
N
×
M
N×M 的矩阵。若
G
i
,
j
=
1
G
i,j
​
 =1 表示其为道路，否则表示其为障碍物。

最后一行输入四个整数
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
 ，表示入口的位置和出口的位置。

1
≤
N
,
M
≤
1
0
2
1≤N,M≤10
2
 ，
0
≤
G
i
,
j
≤
1
0≤G
i,j
​
 ≤1，
1
≤
x
1
,
x
2
≤
N
1≤x
1
​
 ,x
2
​
 ≤N，
1
≤
y
1
,
y
2
≤
M
1≤y
1
​
 ,y
2
​
 ≤M。

输出描述
输出仅一行，包含一个整数表示答案。

若无法从入口到出口，则输出
−
1
−1。

输入输出样例
示例 1
输入

5 5
1 0 1 1 0
1 1 0 1 1
0 1 0 1 1
1 1 1 1 1
1 0 0 0 1
1 1 5 5

输出

8


"""

from collections import deque

# 读取矩阵的大小 n 和 m
n, m = map(int, input().split())

# 初始化一个空矩阵
matrix = []

# 逐行输入矩阵的元素
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

x1, y1, x2, y2 = map(int, input().split())
# 定义上下左右
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# 转化坐标
start = (x1-1, y1-1)
end = (x2-1, y2-1)

# 队列，用来保存待访问的节点（每个节点为 (x, y, 步数)）
queue = deque([(start[0], start[1], 0)])  # 起点加入队列，步数为0

# 创建访问记录数组
visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True  # 标记起点为已访问

# 是否能到出口
flag = 0

while queue:
    x, y, step = queue.popleft()
    # 如果当前节点是终点，返回步数
    print("当前节点为", x, y, step)
    print(end)
    if (x, y) == end:
        flag = 1
        print(step)
        break
    for (dx, dy) in directions:
        nx, ny = dx + x, dy + y
        if 0 <= nx < n and 0 <= ny < m and (x, y) and visited[nx][ny]==False and matrix[nx][ny] == 1:
            queue.append((nx, ny, step + 1))  # 将邻居加入队列，步数加1
            visited[nx][ny] = True

if flag == 0:
    print("-1")
