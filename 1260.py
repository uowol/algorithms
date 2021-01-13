import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().rstrip().split(' '))
node = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().rstrip().split(' '))
    node[A].append(B)
    node[B].append(A)

for i in range(N):
    node[i+1].sort()

stack = deque([])
queue = deque([])
# print(node)

def dfs(v):
    if v in visit: 
        if len(stack) > 0:
            dfs(stack.pop())
        return()
    print(v, end=" ")
    visit.append(v)
    for i in range(len(node[v])-1, -1, -1):
        if not node[v][i] in visit:
            stack.append(node[v][i])
    if len(stack) > 0:
        dfs(stack.pop())

def bfs(v):
    if v in visit: return()
    print(v, end=" ")
    visit.append(v)
    for i in node[v]:
        if not i in queue and not i in visit:
            queue.append(i)
    if len(queue) > 0:
        bfs(queue.popleft())


visit = []
dfs(V)
print()
visit = []
bfs(V)
