import sys

N = int(sys.stdin.readline())

a = [0 for i in range(41)]
a[0] = 1
a[1] = 0

for i in range(2, 41):
    a[i] = a[i-1] + a[i-2]

for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        print("1 0")
    else: print(a[n], a[n-1] + a[n])