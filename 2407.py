import sys
# from collections import deque
import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dp = [0 for _ in range(N)] 

for i in range(1, N):
    dp[i] = [0 for _ in range(i+1)]
    for j in range(i+1):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

# print(dp)
print(dp[N-1][M-1] + dp[N-1][M])



