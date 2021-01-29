import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

queue = deque([N])
hist = [0 for i in range(1000001)]
hist[N] = 1

def bfs(cnt, queue, target):
    new_queue = deque([])
    while len(queue) > 0:
        now = queue.popleft()
        if now == target: return cnt
        if now-1 >= 0 and not hist[now-1]:
            new_queue.append(now-1)
            hist[now-1] = 1
        if not hist[now+1]:
            new_queue.append(now+1)
            hist[now+1] = 1
        if now*2 < 1000000 and not hist[now*2]:
            new_queue.append(now*2)
            hist[now*2] = 1

    queue = new_queue
    return bfs(cnt+1, queue, target)

if M <= N:
    print(N-M)
else:
    print(bfs(0, queue, M))

