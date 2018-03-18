import time
import copy

a = [0]
for i in range(1000):
    a.append(i)

t00 = time.perf_counter()

b = copy.copy(a)

t01 = time.perf_counter()

c = copy.deepcopy(a)

t02 = time.perf_counter()

print("%9.1f ns" % ((t01 - t00) * 1000000))
print("%9.1f ns" % ((t02 - t01) * 1000000))
