import sys
from collections import deque
# import heapq

sys.setrecursionlimit(100)

def input():
    return sys.stdin.readline().rstrip()

w = int(input())
sea = [None for _ in range(w)]
pos = [-1, -1]
size = 2
cnt_eat = 0

for i in range(w):
    sea[i] = list(map(int, input().split()))
    for j in range(w):
        if sea[i][j] == 9:
            pos = [i, j]
            sea[i][j] = 0

def canPass(position):
    global size, sea
    if sea[position[1]][position[0]] <= size:
        return True
    return False

cnt_bfs = 0
complete_bfs = False

def bfs_search(queue, footprints):
    global sea, cnt_bfs, pos

    next_queue = deque([])
    fish = []

    while len(queue) > 0:
        y, x = queue.popleft()

        if sea[y][x] != 0 and sea[y][x] < size:
            fish.append([y, x])

        footprints[y][x] = 1

        if x-1 >= 0 and canPass([x-1, y]) and not footprints[y][x-1]:
            next_queue.append([y, x-1])
            footprints[y][x-1] = 1
        if x+1 < w and canPass([x+1, y]) and not footprints[y][x+1]:
            next_queue.append([y, x+1])
            footprints[y][x+1] = 1
        if y-1 >= 0 and canPass([x, y-1]) and not footprints[y-1][x]:
            next_queue.append([y-1, x])
            footprints[y-1][x] = 1
        if y+1 < w and canPass([x, y+1]) and not footprints[y+1][x]:
            next_queue.append([y+1, x])
            footprints[y+1][x] = 1
    
    if len(fish) > 0:
        y, x = min(fish)
        sea[y][x] = 0
        pos = [y, x]
        return cnt_bfs

    if len(next_queue) == 0:
        return False

    cnt_bfs += 1
    return bfs_search(next_queue, footprints)

cnt_timer = 0

while True:
    cnt_bfs = 0
    res = bfs_search(deque([pos]), [[0 for _ in range(w)] for _ in range(w)])

    if res:
        cnt_timer += res
        cnt_eat += 1
        if cnt_eat == size:
            cnt_eat = 0
            size += 1
    else: break

    # print(res, cnt_eat, size)

print(cnt_timer)