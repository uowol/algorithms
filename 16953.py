import sys
from collections import deque
# import heapq

sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

def bfs(s_num, e_num):
    queue = deque([s_num])
    cnt_loop = 1
    cnt = 0
    while len(queue) > 0:
        num = queue.popleft()
        if num == e_num:
            return cnt+1
        if num < e_num:
            queue.append(num * 2)
            queue.append(num * 10 + 1)
        cnt_loop -= 1
        if cnt_loop == 0:
            cnt += 1
            cnt_loop = len(queue)
    return -1

a, b = map(int, input().split())

print(bfs(a, b))
