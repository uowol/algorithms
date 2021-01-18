testcase = '''9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
'''

import sys
input = sys.stdin.readline

N = int(input())
paper = [0 for i in range(N)]

for i in range(N):
    paper[i] = list(map(int, input().rstrip().split(' ')))

def recursiveFunction(x,y,w):
    target = paper[y][x]
    for i in range(w):
        for j in range(w):
            if paper[y+i][x+j] != target:
                a,b,c = (0, 0, 0)
                w = int(w/3)
                res = recursiveFunction(x,y,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x+w,y,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x+2*w,y,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x,y+w,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x+w,y+w,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x+2*w,y+w,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x,y+2*w,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x+w,y+2*w,w)
                a += res[0]
                b += res[1]
                c += res[2]
                res = recursiveFunction(x+2*w,y+2*w,w)
                a += res[0]
                b += res[1]
                c += res[2]
                return([a,b,c])                
    res = [0,0,0]
    res[target+1] += 1
    return(res)
                
for r in recursiveFunction(0,0,N):
    print(r)
