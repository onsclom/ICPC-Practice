import math
import sys

for line in sys.stdin:
    n = int(line)
    print(math.ceil((n-1)-(n-1)/math.sqrt(2)))