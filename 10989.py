import sys
# from collections import deque
import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = [0] * 10001

for i in range(N):
    arr[int(input())] += 1

for i in range(10000+1):
    for _ in range(arr[i]):
        print(i)
