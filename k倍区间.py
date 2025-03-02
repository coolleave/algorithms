n, k = list(map(int, input().split()))
lst = []
sum = [0] * n
for i in range(n):
    num = int(input())
    lst.append(num)
    if i == 0:
        sum[0] = num
    else:
        sum[i] = sum[i - 1] + num
total = 0
# print(lst)
# print(sum)
for a in range(len(sum)):
    if sum[a] % k == 0:
        total += 1
    for b in range(a + 1, len(sum)):
        if (sum[b] - sum[a]) % k == 0:
            # print(b, a)
            total += 1
print(total)
