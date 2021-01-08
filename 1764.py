# 듣보잡
import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

answer = []
unknowns = [None for i in range(N)]

def search(str, arr, left, right):
    mid = (left + right)//2
    if arr[mid] == str:
        return True
    if left == right:
        return False
    if arr[mid] < str:
        return search(str, arr, mid+1, right)
    else:
        return search(str, arr, left, mid-1)

for i in range(N):
    unknowns[i] = sys.stdin.readline().rstrip()

unknowns.sort()

cnt = 0
for i in range(M):
    ipt = sys.stdin.readline().rstrip()
    if search(ipt, unknowns, 0, N-1):
        answer.append(ipt)
        cnt+=1

print(cnt)
for man in answer:
    print(man)