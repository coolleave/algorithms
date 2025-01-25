"""
水仙花数
自幂数它的每个位上的数字的 n 次幂之和等于它本身。
用pow
"""

num = int(input())
if num == pow(num // 100, 3) + pow((num // 10) % 10, 3) + pow(num % 10, 3):
    print("YES")
else:
    print("NO")
