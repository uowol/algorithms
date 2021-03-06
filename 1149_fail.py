import sys
# from collections import deque
# import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

house = [None for _ in range(n)]
for i in range(n):
    house[i] = list(map(int, input().split())) 

for i in range(1, n):
    house[i][0] = house[i][0] + min(house[i-1][1], house[i-1][2])
    house[i][1] = house[i][1] + min(house[i-1][0], house[i-1][2])
    house[i][2] = house[i][2] + min(house[i-1][1], house[i-1][0])

print(min(house[n-1]))