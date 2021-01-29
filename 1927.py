import heapq
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    ipt = int(input())
    if ipt == 0:
        if len(heap) == 0: print(0)
        else: print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, ipt)