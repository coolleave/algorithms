import math

total = 23333333

# 1出现的次数
for i in range(total//2, total):
    # x1的比例
    x1 = i / total
    # x0 的比例
    x0 = 1 - i / total
    # 判断
    if round(x1 * i * math.log2(x1) + x0 * (total-i) * math.log2(x0), 4) == -11625907.5798:
        print(total - i)
        break
