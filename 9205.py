import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def manhattan(A, B):
    return (abs(B[0]-A[0]) + abs(B[1] - A[1]))

def bfs(queue, conv, end):
    while len(queue) > 0:
        now = queue.popleft()
        for destination in conv:
            if destination[2]: continue
            if manhattan(now, destination) <= 1000:
                if destination[0] == end[0] and destination[1] == end[1]: return True
                queue.append(destination)
                destination[2] = 1
    return False                                                                                                                                                                                                                        
    

T = int(input())

for t in range(T):
    n = int(input())
    conv = [0 for i in range(n+2)]
    for i in range(n+2):
        conv[i] = list(map(int, input().rstrip().split())) + [0]
    
    queue = deque([conv[0]])
    conv[0][2] = 1

    result = bfs(queue, conv, conv[n+1])

    if result:
        print('happy')
    else:
        print('sad')
