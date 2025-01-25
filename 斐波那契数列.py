"""
斐波那契数列
"""

n = int(input())
x = 1
y = 1
z = 0
print(1)
print(1)
for i in range(n-2):
    z = x + y
    x = y
    y = z
    print(z)


