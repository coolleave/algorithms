import os
import sys

l,n = list(map(int,input().split()))
lst = list(map(int,input().split()))
total = sum(lst)
def add(numnber):
  amount = 0
  for i in range(1,numnber+1):
    flag = 1
    amount = amount + flag*i
    flag = - flag
  return amount
for _ in range(n):
  l,r = list(map(int,input().split()))
  if (r-l+1)%2!=0:
    total = total + l + (r-l) - (r-l+1)//2
  if (r-l+1) % 2 == 0:
    total = total - (r-l+1)//2

print(total)
