num = input()
count = 0

def isHnumber(i):
    global count
    i = str(i)
    for a in range(1, len(i) + 1):
        # 偶数位
        if a % 2 == 0:
            if int(i[a * (-1)]) % 2 != 0:
                return False
        # 奇数位
        else:
            if int(i[a * (-1)]) % 2 != 1:
                return False
    count = count +1


for i in range(1, int(num) + 1):
    isHnumber(i)
print(count)