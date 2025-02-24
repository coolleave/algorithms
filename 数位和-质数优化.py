# 判断是否为质数
def check(n):
    for item in lst:
        # 不为质数
        if n % item == 0:
            return 0
    # 为质数
    lst.append(n)
    count = 0
    for num in str(n):
        count += int(num)
    if count == 23:
        return 1
    else:
        return 0


# 质数列表
lst = [2, 3]
total_count = 0
# 符合条件的数字的数量
for i in range(4, 1000000):
    total_count = total_count + check(i)

print(total_count)
