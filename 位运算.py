
# 利用位运算判断是否为奇偶数
import random


def isObb(n):
    if n & 1:
        print("obb")
    else:
        print("even")


# 利用异或去重
"""
异或 ^   
1^0 = 1; 0^1 = 1; 1^1 = 0; 0^0 = 0;
利用异或可以去重
思路 有n+1个不同的数,在1到n范围内,找出重复一次的数字x0
异或去重 x^x = 0; x^0 = x
(x1^x2^...^xn+1)^(1^2^...^n) = x0

"""


def dr(n):

    # 生成值为1到n的数组
    arr = list(range(1, n + 1))
    # 随机选择一个值插入到数组中，使数组有n+1个元素
    random_value = random.choice(arr)  # 生成随机数
    arr.append(random_value)  # 将随机数添加到数组末尾
    # 随机打乱数组顺序
    random.shuffle(arr)
    print(arr)
    print(random_value)
    x0 = 0
    for x in range(n+1):
        x0 = x0 ^ x  # 1^2^...^n
    for x in arr:
        x0 = x0 ^ x  # (x1^x2^...^xn+1)^(1^2^...^n)

    print(x0)
    print("---------------------方法2———————————————————")
    """
    暴力去重
    """
    helpter = [0] * n  # 初始为n个0的列表
    for i in arr:
        helpter[i-1] = helpter[i-1]+1  # 出现一次，值就加1
    for a in helpter:
        if a == 2:
            print(helpter.index(a)+1)  # 找到值为2的索引


if __name__ == '__main__':
    # isObb(3)
    dr(1000)
