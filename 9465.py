import sys
# from collections import deque
import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    dp = [[], []]
    for i in range(2):
        dp[i] = [0, 0] + list(map(int, input().rstrip().split()))
    for j in range(2, n+2):
        dp[0][j] += max(dp[1][j-1], dp[1][j-2])
        dp[1][j] += max(dp[0][j-1], dp[0][j-2])
    print(max(dp[0][n+1], dp[1][n+1]))