import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w, num_block = map(int, input().rstrip().split())

env = [0 for _ in range(h)]
height = [0 for i in range(256+1)]

num_min = 256
num_max = 0

for i in range(h):
    env[i] = list(map(int, input().rstrip().split()))
    for _height in env[i]:
        if _height < num_min:
            num_min = _height
        if _height > num_max:
            num_max = _height
        height[_height] += 1

# print(num_min, num_max)
# print(num_block)
# print(height)

time = 0
while num_min != num_max:
    time_build = height[num_min]
    time_dig = height[num_max] * 2
    if time_build <= time_dig and height[num_min] <= num_block:
        num_block -= height[num_min]
        time += time_build
        num_min += 1
        height[num_min] += height[num_min - 1]
        height[num_min - 1] = 0
    else:
        num_block += height[num_max]
        time += time_dig
        num_max -= 1
        height[num_max] += height[num_max + 1]
        height[num_max + 1] = 0

print(time, num_max)