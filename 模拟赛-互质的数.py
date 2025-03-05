"""
如果两个整数 a,b除了1以外，没有其它的公约数，则称整数a与b互质。
请问，与 2024 互质的数(包括1)中，第2024 小的是多少?
"""
lst = [2, 11, 23]
count = 0
for i in range(10000000):
    flag = 1
    for num in lst:
        if i % num == 0:
            flag = 0
            break
    if flag and i != 2024:
        count += 1
        print(i)
        if count == 2024:
            break
