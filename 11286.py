
import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    ipt = int(input())
    if ipt != 0:
        heapq.heappush(heap, (ipt**2, ipt))
    else:
        if len(heap) == 0: print(0)
        else: print(heapq.heappop(heap)[1])