import math
n = int(input())

def cal(n):
    for i in range(int(math.sqrt(n))+1):
        for j in range(int(math.sqrt(n))+1):
            for m in range(int(math.sqrt(n)+1)):
                for k in range(int(math.sqrt(n)+1)):
                               if i**2 + j ** 2 + m ** 2 +k**2 == n:
                                   print(i,j,m,k)
                                   return ;
cal(n)
