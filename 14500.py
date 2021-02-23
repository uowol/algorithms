import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

h, w = map(int, input().split())

khan = [None for _ in range(h)]
for i in range(h):
    khan[i] = list(map(int, input().split()))




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
