import sys
input = sys.stdin.readline

N = int(input())

def f(n, target):
    if n > target: return 0
    if n == target: return 1
    res = 0
    res += f(n+1, target)
    res += f(n+2, target)
    res += f(n+3, target)
    return res


for i in range(N):
    M = int(input())
    print(f(0, M))