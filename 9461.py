import sys
input = sys.stdin.readline

N = int(input())

hol = [0 for i in range(51)]
hol[0:3] = [1,1,2]
jak = [0 for i in range(51)]
jak[0:3] = [1,2,3]

for i in range(6, 101):
    if i & 1:
        n = i // 2
        jak[n] = hol[n] + hol[n-2]
    else:
        n = i // 2
        hol[n] = jak[n-1] + jak[n-3]

for i in range(N):
    M = int(input())
    n = M // 2
    if M & 1:
        print(hol[n])
    else:
        print(jak[n-1])