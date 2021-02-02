import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().rstrip().split(' '))
    hist = [0 for i in range(N+1)]
    answer = False
    i = 0
    a = M*i + x
    b = a % N
    if b == 0: b = N
    while hist[b] == 0:
        print("b = ", b)
        if b == y:
            print(a)
            answer = True
            break
        hist[b] = 1
        i += 1
        a = M*i + x
        b = a % N
        if b == 0: b = N
    if not answer:
        print(-1)
