import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

people = [i+1 for i in range(n)]
idx = 0
cnt = 0
ans = []

while len(ans) < n:
    # print(idx)
    if people[idx] == -1:
        idx = (idx + 1) % n
        continue
    cnt+=1
    if cnt == k:
        cnt = 0
        ans.append(str(people[idx]))
        people[idx] = -1
    idx = (idx + 1) % n

print('<' + ', '.join(ans) + '>')