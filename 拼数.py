"""
问题描述
给定
n
n 个正整数
a
1
,
a
2
,
…
,
a
n
a
1
​
 ,a
2
​
 ,…,a
n
​
 ，你可以将它们任意排序。

现要将这
n
n 个数字连接成一排，即令相邻数字收尾相接，组成一个数。

问，这个数最大可以是多少。

输入格式
第一行输入一个正整数
n
n（1≤n≤20 1≤n≤20）。

第二行输入
n
n 个正整数a1 a2
（1≤ai≤105）。

输出格式
输出一个整数，表示答案。

样例输入
3
13 312 343
copy
样例输出
34331213
"""

import functools


# 自定义排序
def sort_string(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1  # s1 排在 s2 前边
    else:
        return 1  # s1 排在 s2 后边


n = int(input())
lst = input().split()
lst.sort(key=functools.cmp_to_key(sort_string))
print("".join(lst))

"""
题解思路
python 的字符串 + 符号 是直接拼接
python的字符串比较是基础unicode，从左到右单个字符进行比较unicode码，直到遇到不一样或者完全比较完成为止
例如比较 "432"和 "442"
先比较 "4" 和 "4" 的 unicode 码，相同，继续比较
比较 "3"和"4" 的unicode码，"4"大于"3"，比较完毕，停止比较
"442">"443"

使用python sort的自定义排序方法，将自定义sort_string作为排序规则
排序之后直接拼接即可
"""
