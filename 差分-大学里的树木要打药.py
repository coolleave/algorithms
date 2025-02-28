n, m = list(map(int, input().split()))
total=0
for _ in range(m):
    l, r, p = list(map(int, input().split()))
    total += (r-l+1)*p
print(total)