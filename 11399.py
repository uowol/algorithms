import sys
input = sys.stdin.readline

N = int(input())

people = list(map(int, input().rstrip().split(' ')))
people.sort()
_sum = people[0]
for i in range(1, N):
    people[i] = people[i-1] + people[i]
    _sum += people[i]
print(_sum)
