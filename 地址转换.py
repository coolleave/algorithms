"""
进制转换问题，将10进制转化为26进制
0-A,1-B,2-C,3-D
这里注意，一定是0-A,不是1-A，
还有一个问题，10可以写成 0000010
但这里BA 不能写成AAAAABA

"""
n = int(input())
lst = []
# 因为a对应0  要-1
while n:
    mod = (n-1) % 26
    n = ((n-1) // 26)
    lst.insert(0, mod)
# print(lst)
for i in range(len(lst)):
    print(chr(lst[i] + 65), end='')
