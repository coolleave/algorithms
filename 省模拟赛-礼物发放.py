n = int(input())
exp = list(map(int, input().split()))
m = int(input())
gift = list(map(int, input().split()))
count = 0
j = 0
for i in range(n):
    while 0 <= j < m:
        if exp[i] <= gift[j]:
            count += 1
            j += 1
            break
        else:
            j += 1
print(count)
