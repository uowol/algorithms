import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

miro = [0 for _ in range(N)]
miro_arrive = [[0 for _ in range(M)] for _ in range(N)]
miro_arrive[0][0] = 1

for i in range(N):
    elements = input().rstrip()
    miro[i] = [int(elements[k]) for k in range(M)]

queue = deque([(0, 0)])

def bfs(queue, step):
    next_queue = deque([])
    while len(queue) > 0:
        x, y = queue.popleft()
        # print(x, '/', M, y, '/', N, '=>', step)
        if x == M-1 and y == N-1: return step
        if x-1 >= 0 and miro[y][x-1] and not miro_arrive[y][x-1]:
            next_queue.append((x-1, y))
            miro_arrive[y][x-1] = 1
        if x+1 < M and miro[y][x+1] and not miro_arrive[y][x+1]:
            next_queue.append((x+1, y))
            miro_arrive[y][x+1] = 1
        if y-1 >= 0 and miro[y-1][x] and not miro_arrive[y-1][x]:
            next_queue.append((x, y-1))
            miro_arrive[y-1][x] = 1
        if y+1 < N and miro[y+1][x] and not miro_arrive[y+1][x]:
            next_queue.append((x, y+1))
            miro_arrive[y+1][x] = 1
    return bfs(next_queue, step+1)

print(bfs(queue, 1))
        