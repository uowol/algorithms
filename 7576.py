import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().rstrip().split(' '))
cnt_zero = 0

box = [0 for _ in range(N)]
for i in range(N):
    box[i] = list(map(int, input().rstrip().split(' ')))


queue = deque([])

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            queue.append([x,y])
        elif box[y][x] == 0:
            cnt_zero += 1

def bfs(queue, box, m, n):
    global cnt_zero

    day = 0
    size = len(queue)
    cnt = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        if size==cnt:
            day += 1
            size = len(queue)
            cnt = 0
        x,y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if box[ny][nx]==0:
                    box[ny][nx]=1
                    queue.append([nx,ny])
                    cnt_zero -= 1
    return day

    # # print(queue)
    # global cnt_zero
    # next_queue = deque([])
    # if len(queue) == 0:
    #     return cnt-1
    # while len(queue) > 0:
    #     x, y = queue.popleft()
    #     if x-1 >= 0 and box[y][x-1] == 0:
    #         cnt_zero -= 1
    #         next_queue.append([x-1,y])
    #         box[y][x-1] = 1
    #     if x+1 < M and box[y][x+1] == 0:
    #         cnt_zero -= 1
    #         next_queue.append([x+1,y])
    #         box[y][x+1] = 1
    #     if y-1 >= 0 and box[y-1][x] == 0:
    #         cnt_zero -= 1
    #         next_queue.append([x,y-1])
    #         box[y-1][x] = 1
    #     if y+1 < N and box[y+1][x] == 0:
    #         cnt_zero -= 1
    #         next_queue.append([x,y+1])
    #         box[y+1][x] = 1
    # return bfs(cnt + 1, next_queue, box)

if cnt_zero == 0:
    print(0)
else:
    cnt = bfs(queue, box, M, N)

    # print(cnt_zero)

    if cnt_zero == 0:
        print(cnt)
    else: print(-1)
