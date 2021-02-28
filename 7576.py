import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().rstrip().split(' '))
cnt_all = 0

box = [0 for _ in range(N)]
for i in range(N):
    box[i] = list(map(int, input().rstrip().split(' ')))


queue = deque([])

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            queue.append([x,y])
            cnt_all += 1
        if box[y][x] == -1:
            cnt_all += 1

def bfs(cnt, queue, box):
    print(queue)
    global cnt_all
    next_queue = deque([])
    if len(queue) == 0:
        return cnt-1
    while len(queue) > 0:
        x, y = queue.popleft()
        if x-1 >= 0 and box[y][x-1] == 0:
            cnt_all += 1
            next_queue.append([x-1,y])
            box[y][x-1] = 1
        if x+1 < M and box[y][x+1] == 0:
            cnt_all += 1
            next_queue.append([x+1,y])
            box[y][x+1] = 1
        if y-1 >= 0 and box[y-1][x] == 0:
            cnt_all += 1
            next_queue.append([x,y-1])
            box[y-1][x] = 1
        if y+1 < N and box[y+1][x] == 0:
            cnt_all += 1
            next_queue.append([x,y+1])
            box[y+1][x] = 1
    return bfs(cnt + 1, next_queue, box)

if cnt_all == M*N:
    print(0)
else:
    cnt = bfs(0, queue, box)

    # print(cnt_all)

    if cnt_all == M*N:
        print(cnt)
    else: print(-1)
