import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().rstrip().split(' '))

coins = [0 for _ in range(N)]

idx = 0

for i in range(N):
    coins[i] = int(input())
    if coins[i] <= K:
        idx = i

money = K
cnt = 0
while money > 0:
    cnt += money//coins[idx]
    money = money % coins[idx]
    idx -= 1

print(cnt)