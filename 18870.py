import sys

input = sys.stdin.readline

N = int(input())

X = list(map(int, input().rstrip().split(' ')))

idx = {}

i = 0
for x in X:
    if not x in idx:
        idx[x] = []
    idx[x].append(i)
    i+=1

sorted_X = sorted(list(set(X)))
res = [0 for i in range(N)]

i = 0
for x in sorted_X:
    for j in idx[x]:
        res[j] = str(i)
    i+=1

print(" ".join(res))


