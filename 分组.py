n = int(input())
lst = list(map(int, input().split()))

lst.sort()
ans = 0
left = 0
right = n // 2
while left < n // 2 and right < n:
    if lst[left] * 2 < lst[right]:
        ans += 1
        left += 1
    right += 1
print(ans)