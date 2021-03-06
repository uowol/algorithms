import sys
# from collections import deque
# import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

arr_num = sorted(set(map(int, input().split())))
res = []
def dfs(arr_num, ret, before):
    global n, m
    if len(ret) == m:
        res.append(ret)
        return
    for i in range(before, len(arr_num)):
        num = arr_num[i]
        dfs(arr_num, ret + [num], i)

for i in range(len(arr_num)):
    num = arr_num[i]
    dfs(arr_num, [num], i)

for num in res:
    print(' '.join(map(str, num)))