# 비밀번호 찾가
import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

dic = {}
for i in range(N):
    site, pw = sys.stdin.readline().rstrip().split(' ')
    dic[site] = pw

for i in range(M):
    print(dic[sys.stdin.readline().rstrip()])