import sys
# from collections import deque
import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

arr = [0] * n
mode = [0,[]]
mode_arr = [0] * 8001

for i in range(n):
    ipt = int(input())
    arr[i] = ipt
    mode_arr[ipt+4000] += 1
    if mode_arr[ipt+4000] > mode[0]:
        mode[0] = mode_arr[ipt+4000]
        mode[1] = [ipt]
    elif mode_arr[ipt+4000] == mode[0]:
        heapq.heappush(mode[1], ipt)

# print('=>', mode)

print(round(sum(arr)/n))
print(sorted(arr)[n//2])
if len(mode[1]) > 1:
    heapq.heappop(mode[1])
print(heapq.heappop(mode[1]))
print(max(arr) - min(arr))