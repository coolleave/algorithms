"""
问题描述
如果一个数p是个质数，同时又是整数a的约数，则p称为
a的一个质因数。
请问，2024的所有质因数的和是多少？
答案提交
这是一道结果填空的题，你只需要算出结果后提交即可。本
题的结果为一个整数，在提交答案时只填写这个整数，填写
多余的内容将无法得分。
"""
lst = [2, 11, 23]
for i in range(2, 2024):
    if 2024 % i == 0 and i % 2 != 0:
        lst.append(i)
print(lst)
print(2+11+23)