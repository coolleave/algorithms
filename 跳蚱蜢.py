from collections import deque

# 初始位置
s0 = '012345678'
# 最终位置
s = '876543210'

visiabled = set()
step = 0  # 需要跳的步数
index = 0  # 当前0的索引
queue = deque([(s0, index, step)])
# 将初始状态加入已访问集合
visiabled.add(s0)

while queue:
    # 取出
    s1, index, step = queue.popleft()

    if s1 == s:
        print(step)
        break
    # 计算坐标,四种跳法分别为 左1 左2 右1 右2
    for i in range(4):
        if i == 0:
            nindex = (index - 1 + 9) % 9
        elif i == 1:
            nindex = (index - 2 + 9) % 9
        elif i == 2:
            nindex = (index + 1 + 9) % 9
        elif i == 3:
            nindex = (index + 2 + 9) % 9

        # 交换值
        # 将字符串转换为列表（字符串不可变，但列表可变）
        s1_list = list(s1)

        # 执行交换操作
        s1_list[index], s1_list[nindex] = s1_list[nindex], s1_list[index]
        # 将列表转换回字符串
        new_s1 = ''.join(s1_list)

        if new_s1 not in visiabled:
            visiabled.add(new_s1)
            queue.append((new_s1, nindex, step + 1))
