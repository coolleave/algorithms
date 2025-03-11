import time

y = 0
time1 = time.time()
for i in range(10000000000):
    y = 1
time2 = time.time()
print(time2 - time1)
