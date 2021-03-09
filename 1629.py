import sys
# from collections import deque
# import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
hist = [0 for _ in range(10000)]

def divide(a, n):
    global c, hist
    if n < 10000 and hist[n]:
        return hist[n]
    if n == 1:
        return a % c
    if n & 1:
        if n < 10000: 
            res = conquer(divide(a, n//2)*divide(a, n//2)*divide(a, 1), c)
            hist[n] = res
            return res
        return conquer(divide(a, n//2)*divide(a, n//2)*divide(a, 1), c)
    else:
        if n < 10000: 
            res = conquer(divide(a, n//2)*divide(a, n//2), c)
            hist[n] = res
            return res
        return conquer(divide(a, n//2)*divide(a, n//2), c)

def conquer(a, c):
    return a % c

print(divide(a, b))
