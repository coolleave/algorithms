N, Q = map(int, input().split())
a = list(map(int, input().split()))
dx = [0 for i in range(N + 1)]
for i in range(Q):
    l, r, x = map(int, input().split())
    dx[l - 1] += x
    dx[r] -= x
for i in range(1, N):
    dx[i] += dx[i - 1]
for i in range(N):
    print(max(dx[i] + a[i], 0), end=" ")
