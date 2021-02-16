import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().rstrip().split()))
cards_dict = dict()
for card in cards:
    if str(card) in cards_dict:
        cards_dict[str(card)] += 1
    else:
        cards_dict[str(card)] = 1

m = int(input())

ishave = list(map(int, input().rstrip().split()))
for check in ishave:
    if str(check) in cards_dict:
        print(cards_dict[str(check)], end=' ')
    else:
        print(0, end=' ')

# print(cards_dict)
