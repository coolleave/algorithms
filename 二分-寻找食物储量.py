def find():
    n = int(input())
    lst = list(map(int, input().split()))
    x = int(input())
    left = 0
    right = n - 1
    flag = 0
    while left <= right:
        if lst[n - 1] < x:
            print(-1)
            return
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid + 1
        if lst[mid] > x:
            right = mid - 1
    print(right + 2)


find()
