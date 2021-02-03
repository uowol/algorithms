import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split(' '))

box = [0 for _ in range(H)]

for h in range(H):
    _box = [0 for _ in range(N)]
    for i in range(N):
        _box[i] = list(map(int, input().rstrip().split(' ')))
    box[h] = _box

queue = deque([])

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append([x,y,z])

def bfs(cnt, queue):
    next_queue = deque([])
    if len(queue) == 0:
        return cnt-1
    while len(queue) > 0:
        x, y, z = queue.popleft()
        if x-1 >= 0 and not box[z][y][x-1] and not box[z][y][x-1] == -1:
            next_queue.append([x-1,y,z])
            box[z][y][x-1] = 1
        if x+1 < M and not box[z][y][x+1] and not box[z][y][x+1] == -1:
            next_queue.append([x+1,y,z])
            box[z][y][x+1] = 1
        if y-1 >= 0 and not box[z][y-1][x] and not box[z][y-1][x] == -1:
            next_queue.append([x,y-1,z])
            box[z][y-1][x] = 1
        if y+1 < N and not box[z][y+1][x] and not box[z][y+1][x] == -1:
            next_queue.append([x,y+1,z])
            box[z][y+1][x] = 1
        if z-1 >= 0 and not box[z-1][y][x] and not box[z-1][y][x] == -1:
            next_queue.append([x,y,z-1])
            box[z-1][y][x] = 1
        if z+1 < H and not box[z+1][y][x] and not box[z+1][y][x] == -1:
            next_queue.append([x,y,z+1])
            box[z+1][y][x] = 1
    return bfs(cnt + 1, next_queue)

cnt = bfs(0, queue)

answer = False
for z in range(H):
    if answer: break
    for y in range(N):
        if answer: break
        for x in range(M):
            if box[z][y][x] == 0:
                print(-1)
                answer = True
                break

if not answer: print(cnt)