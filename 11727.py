import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for i in range(N+1)]
dp[1:3] = [1,3]

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[N]%10007)