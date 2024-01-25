import math
import hashlib

precision = 8 # Define precision value

class HyperLogLog:

    def __init__(self, precision):
        self.m = 2 ** precision 
        self.M = [0] * self.m

    def add(self, element):
        x = hashlib.sha1(str(element).encode('utf-8')).hexdigest()
        index = int(x[0:precision], 16) 
        rank = len(x) - len(x.lstrip('0'))
        self.M[index] = max(self.M[index], rank + 1)

    def estimate(self):
        E = float(0.7213 / (1 + 1.079 / self.m))
        summation = 0
        for x in self.M:
            summation += 1.0 / float(2 ** x)
        Est = self.m * math.log(summation)
        return round(E * Est)

hll = HyperLogLog(precision) 

hll.add("cat")  
hll.add("dog")
hll.add("fish") 
hll.add("cat")

print(hll.estimate())