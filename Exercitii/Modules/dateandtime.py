import random
import time
from datetime import datetime


#now = time.time()

#print(now)

l1 = [random.randint(1, 9999) for i in range(1000)]

start = time.time()
l1.sort()
stop = time.time()
print(f"Executia a drat {stop - start} s")