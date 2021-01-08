# 브루트포스
import sys

n = int(sys.stdin.readline())

squares = [i for i in range(n+1)]

for i in range(2, n+1):
    root = int(i**0.5)
    if root**2 == i: 
        squares[i] = 1
        next
    for j in range(1, root+1):
        squares[i] = min(squares[i], squares[i - j**2] + 1)

print(squares[n])
