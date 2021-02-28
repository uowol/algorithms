import sys
from collections import deque
from itertools import combinations
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

# def combine(arr, n):
#     if len(arr) <= n:
#         return [arr]
#     ret = []
#     m = len(arr)
#     pivot = [i for i in range(n)]
#     # print(arr, n, pivot)

#     while pivot[0] < m-n:
#         tmp_arr = []
#         cnt_tmp = 0
#         for i in range(n-1, 0, -1):
#             while pivot[i] >= m and cnt_tmp<100:
#                 # print(pivot)
#                 cnt_tmp+=1
#                 for j in range(1, i+1):
#                     if pivot[j] >= m:
#                         pivot[j-1] += 1
#                         for k in range(j, i+1):
#                             pivot[k] = pivot[k-1]+1 
#             tmp_arr.append(arr[pivot[i]])
#         tmp_arr.append(arr[pivot[0]])
#         # print(tmp_arr, pivot)
#         pivot[n-1] += 1
#         ret.append(tmp_arr)
#         # print(pivot)
#     # print(ret)
#     return ret

n, m = map(int, input().split())
chicken = []
home = []
for i in range(n):
    info = list(map(int, input().split()))
    for j in range(n):
        if info[j] == 1: home.append([i, j])
        if info[j] == 2: chicken.append([i, j])

# def bfs(queue, loadmap, dist, visit):
#     global n
#     next_queue = deque([])
#     # if len(queue) == 0: return False
#     while len(queue) > 0:
#         i, j = queue.popleft()
#         visit[i][j] = 1
#         if loadmap[i][j] == 1:
#             return dist
#         if i > 0 and not visit[i-1][j]:
#             next_queue.append([i-1, j])
#             visit[i-1][j] = 1
#         if i+1 < n and not visit[i+1][j]:
#             next_queue.append([i+1, j])
#             visit[i+1][j] = 1
#         if j > 0 and not visit[i][j-1]:
#             next_queue.append([i, j-1])
#             visit[i][j-1] = 1
#         if j+1 < n and not visit[i][j+1]:
#             next_queue.append([i, j+1])
#             visit[i][j+1] = 1
#     return bfs(next_queue, loadmap, dist+1, visit)

def dist(a, b):
    # print(a,'-',b, (abs(a[0]-b[0]) + abs(a[1]-b[1])))
    return (abs(a[0]-b[0]) + abs(a[1]-b[1]))

def min_dist(home, chicken):
    res = min(map(lambda x: dist(x,home), chicken))
    return res

_min = 10**6
# print(chicken)
c_chicken = combinations(chicken, m)
for _case in c_chicken:
    sum_dist = 0
    # print(_case)
    for h in home:
        # print('!',min_dist(h, _case))
        sum_dist += min_dist(h, _case)
    # print(sum_dist)
    if sum_dist < _min:
        _min = sum_dist

print(_min)
