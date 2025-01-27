"""
压缩字符串

题目描述
实现一个算法来压缩一个字符串。压缩的要求如下：

需要判断压缩能不能节省空间，仅在压缩后字符串比原字符串长度更短时进行压缩。

压缩的格式是将连续相同字符替换为字符 + 数字形式，例如 "AAABCCDDDD" 变为 "A3BC2D4"。

输入描述
输入一行字符串，长度不超过 500.

输出描述
输出一行。若输入的字符串可压缩，则输出压缩后的字符串，否则输出 NO。

输入输出样例
示例
输入

AAABCCDDDD
copy
输出

A3BC2D4
"""


def compress_string(s):
    n = len(s)
    compressed = []
    count = 1

    # 遍历字符串，统计连续相同字符的个数
    for i in range(n):
        # 如果当前字符和下一个字符相同，增加计数
        if i < n - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            # 如果当前字符和下一个字符不同，将字符和计数加入压缩结果
            if count == 1:
                compressed.append(s[i])
            else:
                compressed.append(f"{s[i]}{count}")
            count = 1  # 重置计数

    # 将压缩结果转换为字符串
    compressed_str = ''.join(compressed)

    # 判断压缩后的字符串是否比原字符串更短
    if len(compressed_str) < n:
        return compressed_str
    else:
        return "NO"


# 输入
s = input().strip()

# 压缩字符串并输出结果
result = compress_string(s)
print(result)
