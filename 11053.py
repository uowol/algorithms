import sys
# from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

n = int(input())
arr = list(map(lambda x: int(x), input().split()))

dp = [[] for _ in range(n+1)]
# print(len(dp), dp)
dp[1] = [arr[0]]

limit = 2

for i in range(n):
    num = arr[i]
    if num < dp[1][0]: dp[1] = [num]
    for j in range(2, limit+1):
        before = dp[j-1]
        # print(num, before, j)
        if num > max(before):
            if len(dp[j]) == 0: 
                dp[j] = before + [num]
                if limit < len(dp[j]) + 1:
                    limit = len(dp[j]) + 1
            elif max(dp[j]) > num: 
                dp[j] = before + [num]
                if limit < len(dp[j]) + 1:
                    limit = len(dp[j]) + 1
            
print(limit-1)

# print(dp)

