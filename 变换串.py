"""
有一个长度为
n
n 的数字字符串
s
s ，下标从
0
0 开始。

给定
k
k 种交换操作，其中第
i
i 种操作包含两个整数
x
i
,
y
i
x
i
​
 ,y
i
​
 ，执行第
i
i 种操作之后，会导致
s
x
i
s
x
i
​

​
  与
s
y
i
s
y
i
​

​
  交换位置。

请问能否通过有限次的操作次数将
s
s 变为一个不下降字符串，如果可以输出最少操作次数，反之输出 -1。

输入格式
第一行输入一个正整数
n
n，表示字符串
s
s 的长度。

第二行输入一个长度为
n
n 只由数字构成的字符串
s
s。

第三行输入一个整数
k
k，表示操作种类的数量。

接下来
k
k 行，每行两个整数，其中第
i
i 行表示第
i
i 种操作的两个参数
x
i
,
y
i
x
i
​
 ,y
i
​
 。

输出格式
一行一个整数，如果可以通过有限次操作将
s
s 变为不下降字符串，则输出最小操作次数，反之输出 -1。
"""


from collections import deque

# 字符串长度
n = int(input())
# 字符串
s = input()
# 找出结果为不下降字符串
s_sort = "".join(sorted(list(s)))
# 交换个数
k = int(input())
# 交换下标对应关系
swaps = []
# 判重
visiabled = set()
# 交换次数
step = 0
# 接收下标
for _ in range(k):
    (x, y) = map(int, input().split())
    swaps.append((x, y))
flag = 0
# 初始化队列
queue = deque([(s, step)])
visiabled.add(s)
while queue:
    s1, step = queue.popleft()
    if s1 == s_sort:
        flag = 1
        print(step)
        break
    for swap in swaps:
        # 交换
        s1_lst = list(s1)
        s1_lst[swap[0]], s1_lst[swap[1]] = s1_lst[swap[1]], s1_lst[swap[0]]
        new_string = "".join(s1_lst)
        if new_string not in visiabled:
            visiabled.add(new_string)
            queue.append((new_string, step + 1))

if flag == 0:
    print(-1)
