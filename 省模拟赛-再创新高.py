n = int(input())
lst = list(map(int, input().split()))
maxNumber = lst[0]
count = 1
for item in lst:
    if maxNumber < item:
        count += 1
        maxNumber = item
print(count)
