import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for t in range(T):
    n, num_target = map(int, input().split())
    q = deque(list(map(int, input().split())))
    num_max = max(q)
    cnt = 0
    while len(q) > 0:
        output = q.popleft()
        if output != num_max:
            q.append(output)
            num_target -= 1
            if num_target == -1:
                num_target = len(q) - 1
        else:
            cnt += 1
            if num_target == 0:
                break
            num_max = max(q)
            num_target -= 1

    print(cnt)
