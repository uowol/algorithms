import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

class Node:
    def __init__(self, i):
        self.min = i
    
nodes = [Node(i) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().rstrip().split(' '))
    if nodes[b].min < nodes[a].min:
        a, b = b, a
    while nodes[a].min < nodes[b].min:
        tmp = nodes[b].min
        nodes[b].min = nodes[a].min
        b = tmp
        
    nodes[b].min = nodes[a].min

# for node in nodes:
#     print(node.min, end=", ")
# print("")

cnt = 0
for n in range(1, N+1):
    if n == nodes[n].min:
        cnt += 1

print(cnt)