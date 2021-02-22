import sys
from collections import deque
# import heapq

sys.setrecursionlimit(100)

def input():
    return sys.stdin.readline().rstrip()

def D(n):
    return int((2*n) % 10000)

def S(n):
    return n-1 if n > 0 else 9999

def L(n):
    d1 = n // 1000
    num = int(n % 1000)*10 + d1
    return num

def R(n):
    d4 = n % 10
    num = int(n / 10) + d4 * 1000
    return num
    # list_n = toArray(n)
    # list_n.appendleft(list_n.pop())
    # return int(''.join(list_n))

def toArray(n):
    num = deque([])
    while n != 0:
        num.appendleft(str(n%10))
        n = n // 10
    while len(num) < 4:
        num.appendleft(str(0))
    return num

T = int(input())

def bfs(queue, end, hist):
    next_queue = deque([])
    while len(queue) > 0:
        tmp = queue.popleft()
        # print(tmp)
        num, res = tmp[0], tmp[1]
        if num == end: return res
        hist[num] = 1
        d, s, l, r = D(num), S(num), L(num), R(num)
        if not hist[d]:
            next_queue.append([d, res+'D'])
            hist[d] = 1
        if not hist[s]:
            next_queue.append([s, res+'S'])
            hist[s] = 1
        if not hist[l]:
            next_queue.append([l, res+'L'])
            hist[l] = 1
        if not hist[r]:
            next_queue.append([r, res+'R'])
            hist[r] = 1
    return bfs(next_queue, end, hist)

for t in range(T):
    start, end = map(int, input().split())
    q = [start, '']
    print(bfs(deque([q]), end, [0 for i in range(10000)]))
    # print(toArray(start))