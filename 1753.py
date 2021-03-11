import sys
# from collections import deque
import heapq

sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

v,e = map(int, input().split())
s_num = int(input())
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
# print(graph)


def dijkstra(graph, start):
    distances = [float('inf') for _ in range(v+1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while len(queue):
        current_distance, current_destination = heapq.heappop(queue)
        if current_distance > distances[current_destination]: continue
        for i in range(len(graph[current_destination])):
            new_destination = graph[current_destination][i][0]
            distance = current_distance + graph[current_destination][i][1]
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distances[new_destination], new_destination])
    
    return distances

distances = dijkstra(graph, s_num)

for i in range(1, v+1):
    if distances[i] == float('inf'): print('INF')
    else: print(distances[i])

