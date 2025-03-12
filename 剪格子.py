m,n = list(map(int,input().split()))
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
print(lst)
ans = 10**9
total = sum(sum(i) for i in lst)
# 方向,上下左右
directions = [(0,1),(0,-1),(-1,0),(1,0)]
# 判重
visited = set()
visited.add((0,0))
def dfs(x,y,c,s):
    global ans,total
    # 判断是否能一分为2
    if total //2  != total /2:
        print(0)
        return 
    # s的2倍大于sum,剪枝
    if s*2 > total:
        return
    # 满足条件
    if s*2 == total and c<ans:
        ans = c
    # 遍历四个方向
    for direction in directions:
        dx,dy = direction[0],direction[1]
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited:
            visited.add((nx,ny))
            dfs(nx,ny,c+1,s+lst[nx][ny])
            visited.remove((nx,ny))
            
dfs(0,0,1,lst[0][0])
print(ans)
        
    
        
