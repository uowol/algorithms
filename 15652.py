import sys
# from collections import deque
import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().rstrip().split())

num_set = {i+1 for i in range(N)}

res = []

def f(num, num_set):
    global res

    while len(num_set) > 0:
        item = num_set.pop()
        now = num + [item]
        # print(now)
        if len(now) == M:
            heapq.heappush(res, now)
        else:
            f(now, num_set)
        
    

f([], num_set)

while len(res) > 0:
    tmp_res = heapq.heappop(res)
    print(' '.join(map(str, tmp_res)))