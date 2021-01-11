import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    M = int(input())
    closet = {}
    for j in range(M):
        cloth, _type = input().rstrip().split(' ')
        if not _type in closet: closet[_type] = 1
        closet[_type] += 1
    closet = list(closet.values())
    
    cnt = 1
    for n in closet: cnt *= n

    print(cnt-1)