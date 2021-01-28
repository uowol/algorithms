import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
node = [0 for i in range(N)]
for i in range(N):
    node[i] = list(map(int, input().rstrip().split(' ')))

col = 0

def research(start_num, num, arr):
    hist[num] = 1
    for i in range(N):
        arr[i] = arr[i] | node[num][i]
        if node[num][i]:
            if i == start_num or hist[i]: continue
            arr = research(start_num, i, arr)
    return arr

for i in range(N):
    arr = [0 for i in range(N)]
    hist = [0 for i in range(N)]
    res = research(i, i, arr)
    print(' '.join(map(str, res)))