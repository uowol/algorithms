import sys
import heapq

sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

n_city = int(input())
n_bus = int(input())

graph = {node: {} for node in range(1, n_city+1)}

for i in range(n_bus):
    _from, _to, cost = map(int, input().split())
    if _to in graph[_from]:
        if cost < graph[_from][_to]: graph[_from][_to] = cost 
    else:
        graph[_from][_to] = cost 


# print(graph)

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        
        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
            
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances

start, end = map(int, input().split())
print(dijkstra(graph, start)[end])

# print(graph)
