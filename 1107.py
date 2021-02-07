import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dist(a, b):
    return abs(a-b)

N = int(input())
M = int(input())
btn_set = {i for i in range(10)}
btn_set -= set(map(int, input().rstrip().split())) if M else set()

min_cnt = dist(N, 100)

def find(num):
    global min_cnt

    for btn in btn_set:
        tmp_num = num + str(btn)
        min_cnt = min(min_cnt, dist(N, int(tmp_num))+len(tmp_num))
        if len(num) < 6:
            find(tmp_num)

find('') if M < 10 else ''

print(min_cnt)