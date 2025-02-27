"""
程序猿圈子里正在流行一种很新的简写方法：对于一个字符串，只保留首尾字符，将首尾字符之间的所有字符用这部分的长度代替。例如 internation-alization 简写成 i18n，Kubernetes （注意连字符不是字符串的一部分）简写成 K8s, Lanqiao 简写成 L5o 等。

在本题中，我们规定长度大于等于
K
K 的字符串都可以采用这种简写方法（长度小于
K
K 的字符串不配使用这种简写）。

给定一个字符串
S
S 和两个字符
c
1
c
1
​
  和
c
2
c
2
​
  ，请你计算
S
S 有多少个以
c
1
c
1
​
  开头
c
2
c
2
​
  结尾的子串可以采用这种简写？
"""

"""
50得分
# """
# k = int(input())
# s, c1, c2 = list(input().split())
# # 9,7,5,3,1
# start = []
# # 2,4,6,8
# end = []
# total = 0
# for i in range(len(s)):
#     if s[i] == c1:
#         start.append(i)
#     if s[i] == c2:
#         end.append(i)
# for left in start:
#     for right in end:
#         if right - left + 1 >= k:
#             total += 1
#         else:
#             break
# print(total)

"""
100得分 前缀和
"""

k = int(input())
s, c1, c2 = list(input().split())
# 表示前i个有多少个c1
pre = [0] * len(s)
res = 0
for i in range(len(s)):
    pre[i] = pre[i - 1]
    # 如果包含c1 加1
    if c1 == s[i]:
        pre[i] += 1
    # 如果c2 为当前值 且i满足长度
    elif c2 == s[i] and i + 1 - k >= 0:
        # 把所有符合条件的 c1 全部加上
        res += pre[i - k + 1]
print(res)
