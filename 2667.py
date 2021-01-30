import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

address = [0 for i in range(N)]

for i in range(N):
    tmp = input().rstrip()
    address[i] = [int(tmp[k]) for k in range(N)]

def bfs(queue, idx, cnt):
    if len(queue) == 0: return cnt
    next_queue = deque([])
    while len(queue) > 0:
        x, y = queue.popleft()
        if x-1 >= 0 and address[y][x-1] > 0:
            next_queue.append((x-1, y))
            cnt += 1
            address[y][x-1] = -idx
        if x+1 < N and address[y][x+1] > 0:
            next_queue.append((x+1, y))
            cnt += 1
            address[y][x+1] = -idx
        if y-1 >= 0 and address[y-1][x] > 0:
            next_queue.append((x, y-1))
            cnt += 1
            address[y-1][x] = -idx
        if y+1 < N and address[y+1][x] > 0:
            next_queue.append((x, y+1))
            cnt += 1
            address[y+1][x] = -idx
    return bfs(next_queue, idx, cnt)

idx = 1
result = []
for i in range(N):
    for j in range(N):
        if address[i][j] > 0:
            address[i][j] = -idx
            result.append(bfs(deque([(j, i)]), idx, 1))
            idx += 1
# print('\n'.join(list(map(str, address))))
# print(result)

print(len(result))
for n in sorted(result): print(n)
