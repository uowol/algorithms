import sys
# from collections import deque
# import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(a,b,c):
    global dp
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if dp[a][b][c]:
        # print(dp[a][b][c])
        return dp[a][b][c]
    if a<b and b<c:
        return(w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c))
    return(w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1,b-1,c-1))

for a in range(21):
    for b in range(21):
        for c in range(21):
            dp[a][b][c] = w(a,b,c)

a, b, c = map(int, input().split())
while (a,b,c) != (-1,-1,-1):
    res = 'w({0}, {1}, {2}) = {3}'
    print(res.format(a,b,c, w(a,b,c)))
    a, b, c = map(int, input().split())


