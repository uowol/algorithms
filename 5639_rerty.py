def input():
    return sys.stdin.readline().rstrip()

def divide(arr, left, right):
    n = arr[left]
    horizon = None
    # print('===', arr, left, right)
    if left > right: return
    if left == right:
        print(n)
        return
    for i in range(left+1, len(arr)):
        if arr[i] > n:
            horizon = i
            break
    if horizon: 
        divide(arr, left+1, horizon-1)
        divide(arr, horizon, right)
    else:
        divide(arr, left+1, right)
    print(n)

import sys
sys.setrecursionlimit(10**9)

ipt = []
while True:
    try:
        ipt.append(int(input()))
    except:
        break

divide(ipt, 0, len(ipt)-1)