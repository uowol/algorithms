import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

graph = [[0 for _ in range(M)] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().rstrip().split(' '))
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1


k = [0 for i in range(N)]
MIN = 10000000

for i in range(N):
    idx = [0 for _ in range(N)]
    queue = deque([])
    idx[i] = 1
    weight = 1
    for j in range(N):
        if graph[i][j]:
            queue.append(j)
            idx[j] = 1
            k[i] += weight
    weight += 1
    while sum(idx) < N:
        new_queue = deque([])
        while len(queue) > 0:
            now = queue.popleft()
            for j in range(N):
                if graph[now][j] and not idx[j]:
                    new_queue.append(j)
                    idx[j] = 1
                    k[i] += weight
        queue = new_queue
        weight += 1
    if MIN > k[i]:
        MIN = k[i]

# print(k, min(k))        
for i in range(N):
    if k[i] == MIN:
        print(i+1)
        break
