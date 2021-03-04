import sys
# from collections import deque
import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().rstrip().split())
ret = []

def dfs(arr_num, set_num, depth):
    global ret, M
    if depth == M:
        ret.append(arr_num)
    else:
        for num in set_num:
            if num >= arr_num[len(arr_num) - 1]:
                dfs(arr_num + [num], set_num, depth+1)


set_num = sorted(list(map(int, input().split())))
for num in set_num:
    dfs([num], set_num, 1)

for arr_num in ret:
    print(" ".join(list(map(str, arr_num))))