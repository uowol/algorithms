import sys
input = sys.stdin.readline

T = int(input())

stack = []

def isWall(x, y, idx, M, N):
    if x < 0 or x >= M: return(True)
    if y < 0 or y >= N: return(True)
    if idx[y][x]: return(True)
    idx[y][x] = 1
    return(False)

def dfs(x, y, bat, idx, M, N):
    idx[y][x] = 1
    if not isWall(x-1, y, idx, M, N):
        if bat[y][x-1] and [x-1,y] not in stack:
            stack.append([x-1,y])
    if not isWall(x+1, y, idx, M, N):
        if bat[y][x+1] and [x+1,y] not in stack:
            stack.append([x+1,y])
    if not isWall(x, y-1, idx, M, N):
        if bat[y-1][x] and [x,y-1] not in stack:
            stack.append([x,y-1])
    if not isWall(x, y+1, idx, M, N):
        if bat[y+1][x] and [x,y+1] not in stack:    
            stack.append([x,y+1])
    if len(stack) > 0:
        dx, dy = stack.pop()
        dfs(dx, dy, bat, idx, M, N)
    
for t in range(T):
    M, N, K = map(int, input().rstrip().split(' '))
    cnt = 0
    bat = [[0 for i in range(M)] for j in range(N)]
    idx = [[0 for i in range(M)] for j in range(N)]
    for k in range(K):
        x, y = map(int, input().rstrip().split(' '))
        bat[y][x] = 1
    for y in range(N):
        for x in range(M):
            if bat[y][x] and not idx[y][x]: 
                dfs(x, y, bat, idx, M, N)
                cnt += 1
    print(cnt)