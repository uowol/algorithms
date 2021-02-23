import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

h, w = map(int, input().split())

score = [None for _ in range(h)]
for i in range(h):
    score[i] = list(map(int, input().split()))

mino = [
    # I
    [
        [0,0],  # x,y
        [1,0],
        [2,0],
        [3,0],
        [4,1]   # w,h
    ],
    [
        [0,0],
        [0,1],
        [0,2],
        [0,3],
        [1,4]
    ],
    # L
    [
        [0,0],
        [0,1],
        [0,2],
        [1,2],
        [2,3]
    ],
    [
        [0,1],
        [1,1],
        [2,1],
        [2,0],
        [3,2]
    ],
    [
        [0,0],
        [1,0],
        [1,1],
        [1,2],
        [2,3]
    ],
    [
        [0,0],
        [0,1],
        [1,0],
        [2,0],
        [3,2]
    ],
    # J
    [
        [1,0],
        [1,1],
        [0,2],
        [1,2],
        [2,3]
    ],
    [
        [0,0],
        [1,0],
        [2,1],
        [2,0],
        [3,2]
    ],
    [
        [0,0],
        [1,0],
        [0,1],
        [0,2],
        [2,3]
    ],
    [
        [0,0],
        [0,1],
        [1,1],
        [2,1],
        [3,2]
    ],
    # T     
    [
        [0,0],
        [1,0],
        [1,1],
        [2,0],
        [3,2]
    ],
    [
        [0,0],
        [0,1],
        [1,1],
        [0,2],
        [2,3]
    ],
    [
        [0,1],
        [1,1],
        [1,0],
        [2,1],
        [3,2]
    ],
    [
        [1,0],
        [1,1],
        [0,1],
        [1,2],
        [2,3]
    ],
    # S
    [
        [0,0],
        [0,1],
        [1,1],
        [1,2],
        [2,3]
    ],
    [
        [0,1],
        [1,1],
        [1,0],
        [2,0],
        [3,2]
    ],
    # Z
    [
        [1,0],
        [0,1],
        [1,1],
        [0,2],
        [2,3]
    ],
    [
        [0,0],
        [1,1],
        [1,0],
        [2,1],
        [3,2]
    ],
    # O
    [
        [0,0],
        [1,0],
        [1,1],
        [0,1],
        [2,2]
    ]
]

res = []
for block in mino:
    x_max, y_max = block[4]
    # print(w,h,x_max,y_max)
    if x_max <= w and y_max <= h:
        for i in range(h - y_max + 1):
            for j in range(w - x_max + 1):
                tmp_sum = 0
                tmp_sum += score[i + block[0][1]][j + block[0][0]]
                tmp_sum += score[i + block[1][1]][j + block[1][0]]
                tmp_sum += score[i + block[2][1]][j + block[2][0]]
                tmp_sum += score[i + block[3][1]][j + block[3][0]]
                res.append(tmp_sum)
print(max(res))

# def dfs(x, y, visit, cnt):
#     global khan
#     stack = deque([])
#     # x, y = stack.pop()
#     visit[y][x] = 1
#     # print(khan[y][x], end=' + ')
#     if cnt == 4:
#         return khan[y][x]
#     if x > 0 and not visit[y][x-1]:
#         stack.append([x-1, y])
#     if x+1 < w and not visit[y][x+1]:
#         stack.append([x+1, y])
#     if y > 0 and not visit[y-1][x]:
#         stack.append([x, y-1])
#     if y+1 < h and not visit[y+1][x]:
#         stack.append([x, y+1])
#     res = []
#     while len(stack) > 0:
#         nx, ny = stack.pop()
#         res.append(khan[y][x] + dfs(nx, ny, visit, cnt+1))
#         # print(cnt, 'get:', res[len(res)-1])
#     if len(res) > 0:
#         return max(res)
#     else:
#         return 0

# results = []
# for i in range(h):
#     for j in range(w):
#         results.append(dfs(j,i, [[0 for _ in range(w)] for _ in range(h)], 1))

# print(results)

# print(results)
