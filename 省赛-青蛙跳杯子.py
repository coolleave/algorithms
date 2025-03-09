import os
import sys

from collections import deque

init = input()
target = input()

# 判重
visited = set()
visited.add(init)
# 方向
diercitons = [-3,-2,-1,1,2,3]
start = init.index('*')
step = 0
queue = deque([(start,step,init)])

# bfs
while queue:
  # print("visited",visited)
  # print(queue)
  cur,step,scene = queue.popleft()
  print(scene)
  if scene == target:
    print(step)
    break
  for dx in diercitons:
    # print(cur+dx)
    x = cur +dx
    if 0<=x<len(init) :
      # 交换位置
      scene1 = list(scene)
      scene1[cur],scene1[x] = scene1[cur+dx],scene1[cur]
      scene1 = "".join(scene1)
      if scene1 not in visited:
          queue.append([x,step+1,scene1])
          visited.add(scene1)
          
    
