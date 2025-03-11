from collections import deque

lst = []
m, n = map(int, input().split())  # 修正输入顺序
for _ in range(n):
    lst.append(list(map(int, input().split())))


def seperate(lst):
    total = sum(sum(row) for row in lst)
    if total % 2 != 0:
        return 0
    target = total // 2

    # 使用BFS，记录到达每个位置的最大当前值
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_current = [[-1 for _ in range(m)] for _ in range(n)]  # 记录到达每个格子的最大current值

    initial = lst[0][0]
    if initial == target:
        return 1
    queue = deque([(0, 0, initial, 1)])
    max_current[0][0] = initial

    while queue:
        x, y, current, steps = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_current = current + lst[nx][ny]
                if new_current > target:
                    continue
                # 如果新路径的current比之前记录的更大，则更新并加入队列
                if new_current > max_current[nx][ny]:
                    max_current[nx][ny] = new_current
                    if new_current == target:
                        return steps + 1
                    queue.append((nx, ny, new_current, steps + 1))
    return 0


print(seperate(lst))
