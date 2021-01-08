import sys

N = int(sys.stdin.readline())
st = [0 for i in range(N)]
for i in range(N):
    st[i] = int(sys.stdin.readline())

dp = [[0,0] for i in range(N)]

if N == 1:
    print(st[0])
elif N == 2:
    print(st[0]+st[1])
else:
    dp[0] = [st[0], 0]
    dp[1] = [st[0]+st[1], st[1]]
    for i in range(2, N):
        dp[i][0] = dp[i-1][1] + st[i]
        dp[i][1] = max(dp[i-2]) + st[i]
    print(max(dp[N-1][0], dp[N-1][1]))