import random

N = 1000
res = [random.randrange(1,1000) for _ in range(N)]

print(' '.join(list(map(str,res))))