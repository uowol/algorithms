import sys

input = sys.stdin.readline

N = int(input())
com = [i for i in range(N+1)]

M = int(input())

for i in range(M):
    a, b = map(int, input().split(" "))
    if com[a] > com[b]:
        a, b = b, a
    for j in range(1, N+1):
        if j != b and com[j] == com[b]: 
            com[j] = com[a]
    com[b] = com[a]

cnt = 0
for i in range(2, N+1):
    if com[com[i]] == 1: cnt+=1

print(com, cnt)
