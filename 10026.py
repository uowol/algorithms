import sys
from collections import deque
# import heapq

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

draw = [None for _ in range(n)]
for i in range(n):
    draw[i] = list(input())

d1 = [[0 for i in range(n)] for j in range(n)]
d2 = [[0 for i in range(n)] for j in range(n)]
cnt_d1 = 0
cnt_d2 = 0

def bfs1(queue, color):
    global d1, draw
    next_queue = deque([])
    if len(queue) == 0: return True
    while len(queue) > 0:
        x, y = queue.popleft()
        d1[y][x] = 1
        if x > 0 and not d1[y][x-1] and draw[y][x-1] in color:
            next_queue.append([x-1, y])
            d1[y][x-1] = 1
        if x+1 < n and not d1[y][x+1] and draw[y][x+1] in color:
            next_queue.append([x+1, y])
            d1[y][x+1] = 1
        if y > 0 and not d1[y-1][x] and draw[y-1][x] in color:
            next_queue.append([x, y-1])
            d1[y-1][x] = 1
        if y+1 < n and not d1[y+1][x] and draw[y+1][x] in color:
            next_queue.append([x, y+1])
            d1[y+1][x] = 1
    return bfs1(next_queue, color)

def bfs2(queue, color):
    global d2, draw
    next_queue = deque([])
    if len(queue) == 0: return True
    while len(queue) > 0:
        x, y = queue.popleft()
        d2[y][x] = 1
        if x > 0 and not d2[y][x-1] and draw[y][x-1] in color:
            next_queue.append([x-1, y])
            d2[y][x-1] = 1
        if x+1 < n and not d2[y][x+1] and draw[y][x+1] in color:
            next_queue.append([x+1, y])
            d2[y][x+1] = 1
        if y > 0 and not d2[y-1][x] and draw[y-1][x] in color:
            next_queue.append([x, y-1])
            d2[y-1][x] = 1
        if y+1 < n and not d2[y+1][x] and draw[y+1][x] in color:
            next_queue.append([x, y+1])
            d2[y+1][x] = 1
    return bfs2(next_queue, color)
    


def explore(position):
    global draw, d1, d2, cnt_d1, cnt_d2
    x, y = position
    if not d1[y][x]: 
        cnt_d1 += 1
        bfs1(deque([[x, y]]), [draw[y][x]])
        # print('d1', d1)
    if not d2[y][x]: 
        cnt_d2 += 1
        if draw[y][x] == 'R' or draw[y][x] == 'G':
            color = ['R', 'G']
        else:
            color = [draw[y][x]]
        bfs2(deque([[x, y]]), color)
        # print('d2', d2)

for i in range(n):
    for j in range(n):
        explore([j, i])

print(cnt_d1, cnt_d2)