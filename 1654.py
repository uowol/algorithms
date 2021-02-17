import sys
# from collections import deque
# import heapq

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

k, n = map(int, input().split())

arr_len = [0] * k

for i in range(k):
    arr_len[i] = int(input())

left = 1
right = max(arr_len)
answer = 0
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for num_len in arr_len:
        cnt += num_len // mid
    if cnt < n:
        right = mid-1
    else:
        left = mid+1
        answer = mid

# print(left, right, answer)
print(answer)