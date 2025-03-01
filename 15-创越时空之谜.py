def digits(num, base):
    # 各个位数和
    total = 0
    while num > 0:
        a = num % base
        num = num // base
        total += a
    return total


count = 0
for i in range(1, 2025):
    if digits(i, 2) == digits(i, 4):
        count += 1
print(count)
