import sys
# from collections import deque
# import heapq

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

start, end = map(int, input().split())

dp = [i for i in range(end+1)]
dp[1] = -1

for i in range(2, end+1):
    if dp[i] == -1:
        continue
    idx = 2
    while i * idx <= end:
        dp[i*idx] = -1
        idx += 1

for i in range(start, end+1):
    if dp[i] != -1: print(i)