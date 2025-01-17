# 递归求斐波那契数列

def fbnq(n):
    if n == 1 or n == 2:
        return 1
    else:
        cur = fbnq(n-1)+fbnq(n-2)
        return fbnq(n-1)+fbnq(n-2)


if __name__ == '__main__':
    #
    # print(fbnq(3))
    # print(fbnq(2))
    print(fbnq(9))
    # print(fbnq(20))
