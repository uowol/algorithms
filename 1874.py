import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

queue = deque([i+1 for i in range(n)])
stack = []
answer = deque([])
solution = []

for i in range(n):
    answer.append(int(input()))

while len(queue) > 0:
    stack.append(queue.popleft())
    solution.append('+')
    while len(stack) > 0 and stack[len(stack) - 1] == answer[0]:
        stack.pop()
        answer.popleft()
        solution.append('-')

if len(stack) > 0:
    print('NO')
else:
    for i in solution:
        print(i)
