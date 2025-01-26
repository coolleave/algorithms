"""
确定字符串是否是另一个的排列

题目描述
实现一个算法来识别一个字符串
s
t
r
2
str2 是否是另一个字符串
s
t
r
1
str1 的排列。排列的解释如下：如果将
s
t
r
1
str1 的字符拆分开，重新排列后再拼接起来，能够得到
s
t
r
2
str2 ，那么就说字符串
s
t
r
2
str2 是字符串
s
t
r
1
str1 的排列。（不忽略大小写）

如果
s
t
r
2
str2 字符串是
s
t
r
1
str1 字符串的排列，则输出 YES；如果
s
t
r
2
str2 字符串不是
s
t
r
1
str1 字符串的排列，则输出 NO；

输入描述
第一行为字符串
s
t
r
1
str1；

第二行为字符串
s
t
r
2
str2；

字符串长度均不超过 100。

输出描述；
输出一行，如果
s
t
r
2
str2 字符串是
s
t
r
1
str1 字符串的排列，则输出 YES；

如果
s
t
r
2
str2 字符串不是
s
t
r
1
str1 字符串的排列，则输出 NO；

输入输出样例
示例
输入

acb
bac

输出

YES
"""
s1 = input()
s2 = input()
flag = True
for char in s2:
    if char not in s1:
        flag = False
        break
print(flag)
