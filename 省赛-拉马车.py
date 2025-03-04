# 选手牌

s1 = list(input())
s2 = list(input())

# 牌桌
s0 = []
# 出牌者 1为a 0为b
flag = 1
while s1 and s2:
    # print('s0  ', s0)
    # print('s1  ', s1)
    # print('s2  ', s2)
    # print('出牌人', flag)
    # a 出牌
    if flag:
        if s1[0] in s0:
            # 找到牌的索引
            index = s0.index(s1[0])
            # 倒序插入
            s1.append(s1[0])
            s1.pop(0)
            # 列表拼接
            if index == 0:
                s1 = s1 + s0[::-1]
            else:
                s1 = s1 + s0[:index - 1:-1]
            # 保留牌桌前几张牌
            s0 = s0[:index]
        else:
            s0.append(s1[0])
            # 交换出牌顺序
            s1.pop(0)
            flag = 0

    # b 出牌
    else:
        if s2[0] in s0:
            index = s0.index(s2[0])
            s2.append(s2[0])
            s2.pop(0)
            if index == 0:
                s2 = s2 + s0[::-1]
            else:
                s2 = s2 + s0[:index - 1:-1]
            s0 = s0[:index]
            flag = 0
        else:
            s0.append(s2[0])
            s2.pop(0)
            flag = 1

if s1:
    print("".join(s1))
if s2:
    print("".join(s2))
