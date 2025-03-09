s = 'ANQNANBNQNANQNQNBNINQNQNANQNINANQNANBNQNANQNQNBNBNQNQNANQNINANQNANBNQNANQNQNBNINQNQNANQNINBNQNANBNQN'

# 无限小
al = float('-inf')
# 储存答案字符串
answer = ''
count = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if len(s[i:j]) <= 10 and s.count(s[i:j]) * len(s[i:j]) > al:
            al = s.count(s[i:j]) * len(s[i:j])
            answer = s[i:j]
            count += 1
print(answer)
