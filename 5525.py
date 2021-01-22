import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

S = input().rstrip()

target_num = N
cnt = 0
res = 0

for i in range(1, len(S)-1):
    if S[i] == 'O' and S[i-1] == 'I' and S[i+1] == 'I':
        cnt+=1
        if cnt >= target_num:
            res += 1
    elif S[i] == 'I' and S[i-1] == 'O' and S[i+1] == 'O':
        cnt = cnt
    else:
        cnt = 0

print(res)