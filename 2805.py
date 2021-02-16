import sys
# from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

num_tree, want = map(int, input().split())

height = sorted(list(map(int, input().split())))

start = 0
end = max(height)
answer = -1

while end != start:
    total = 0
    new_height = []
    mid = (start+end) // 2
    if answer == mid:
        break
    # total = sum([i-mid if mid < i else 0 for i in height])
    for h in height:
        if h > mid:
            total += h-mid
            new_height.append(h)
    if total >= want:
        start = mid
        answer = mid
        height = new_height
    else:
        end = mid
        answer = mid

print(answer)