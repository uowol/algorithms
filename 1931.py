import sys
input = sys.stdin.readline

N = int(input())

conference = [0 for i in range(N)]

for i in range(N):
    conference[i] = list(map(int, input().rstrip().split(' ')))

conference = sorted(sorted(conference), key=lambda conference: conference[1])

end = conference[0][1]
idx = 1
cnt = 1

while idx < N:
    if conference[idx][0] >= end: 
        end = conference[idx][1]
        cnt += 1
    idx += 1

print(cnt)