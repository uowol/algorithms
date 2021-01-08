import sys


def f(n, num_of_5):
    if n % 5 == 0:
        num_of_5 += 1
        return f(n/5, num_of_5)
    else:
        return (num_of_5)


N = int(sys.stdin.readline())

if N < 5:
    print(0)
else:
    cnt = 0
    for i in range(5, N+1):
        num_of_5 = f(i, 0)
        if num_of_5:
            cnt+=num_of_5

    print(cnt)