import sys
# from collections import deque
# import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

dp = [None for i in range(n)]
for i in range(n):
    dp[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]

print(max(dp[n-1]))