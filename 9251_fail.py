def input():
    return sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(10**9)
from collections import deque
# import heapq

A = deque(list(input()))
B = deque(list(input()))

dp = [[0 for i in range(len(A)+1)] for i in range(len(B)+1)]

for i in range(1, len(B)+1):
    b = B[i-1]
    for j in range(1, len(A)+1):
        a = A[j-1]
        if a == b:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = dp[i-1][j] if dp[i-1][j] > dp[i][j-1] else dp[i][j-1]

# print(dp)
print(dp[len(B)][len(A)])