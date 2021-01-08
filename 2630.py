import sys

input = sys.stdin.readline

N = int(input())
paper = [0 for i in range(N)]

for i in range(N):
    paper[i] = list(map(int, input().split(' ')))

def check(x, y, size):
    color = paper[y][x]
    for i in range(y, y+size):
        for j in range(x, x+size):
            if paper[i][j] != color: return(False)
    return(True)

def f(x, y, size):
    x, y, size = map(int, [x, y, size])

    if check(x, y, size):
        color = paper[y][x]
        if color:
            return([0, 1])
        return([1, 0])
    else:
        w = b = 0
        res = f(x, y, size/2)
        w += res[0]
        b += res[1]
        res = f(x+size/2, y, size/2)
        w += res[0]
        b += res[1]
        res = f(x, y+size/2, size/2)
        w += res[0]
        b += res[1]
        res = f(x+size/2, y+size/2, size/2)
        w += res[0]
        b += res[1]
    return(w, b)
        
res = f(0, 0, N)
print(res[0])
print(res[1])