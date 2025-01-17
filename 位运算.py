# 利用位运算判断是否为奇偶数
def isObb(n):
    if n & 1:
        print("obb")
    else:
        print("even")


if __name__ == '__main__':
    isObb(3)
