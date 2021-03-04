import sys
# from collections import deque
# import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr_num = sorted(list(map(int, input().split())))
ret = []
def dfs(num, arr_num, hist, res):
    global ret, n, m
    if len(res) == m:
        ret.append(res)
    old_num = None
    for i in range(n):  
        num = arr_num[i]
        if not i in hist:
            if num != old_num:
                dfs(num, arr_num, hist + [i], res+[num])
            old_num = num
        # else:


for i in range(n):
    num = arr_num[i]
    if i > 0 and num == arr_num[i-1]: continue
    dfs(num, arr_num, [i], [num])

for num in ret:
    print(' '.join(map(str, num)))
