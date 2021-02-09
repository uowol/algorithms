import sys
# from collections import deque
import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

num_set = set(map(int, input().rstrip().split()))

res = []

def f(num, num_set):
    global res

    for item in num_set:
        now = num + [item]
        # print(now)
        if len(now) == M:
            heapq.heappush(res, now)
        else:
            f(now, num_set-set([item]))

f([], num_set)

while len(res) > 0:
    tmp_res = heapq.heappop(res)
    print(' '.join(map(str, tmp_res)))