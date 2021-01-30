import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

mov = [0 for _ in range(N)]

for i in range(N):
    floor = input().rstrip()
    mov[i] = [floor[j] for j in range(N)]

def quadtree(x, y, size):
    idx = mov[y][x]
    result = ''
    for i in range(size):
        for j in range(size):
            if idx != mov[y+i][x+j]:
                next_size = int(size/2)
                result += '('
                result += quadtree(x,y,next_size)
                result += quadtree(x+next_size,y,next_size)
                result += quadtree(x,y+next_size,next_size)
                result += quadtree(x+next_size,y+next_size,next_size)
                result += ')'
                return result
    return idx

print(quadtree(0,0,N))