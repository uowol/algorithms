import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for t in range(T):
    k = int(input())
    cnt = 0
    min_heap = [[], []] # value, deleted
    max_heap = [[], []]
    for i in range(k):
        cmd, v = input().rstrip().split()
        v = int(v)
        if cmd == 'I':
            heapq.heappush(min_heap[0], v)
            heapq.heappush(max_heap[0], -v)
            cnt+=1
        else:
            if cnt == 0: continue
            if v == 1:
                # tmp_heap_value, tmp_heap_deleted = max_heap[0][:], max_heap[1][:]
                max_value = heapq.heappop(max_heap[0])
                while len(max_heap[1]) > 0 and max_value == max_heap[1][0]:
                    max_value = heapq.heappop(max_heap[0])
                    heapq.heappop(max_heap[1])
                # heapq.heappush(max_heap[1], max_value)
                heapq.heappush(min_heap[1], - max_value)
            else:
                # tmp_heap_value, tmp_heap_deleted = min_heap[0][:], min_heap[1][:]
                min_value = heapq.heappop(min_heap[0])
                while len(min_heap[1]) > 0 and min_value == min_heap[1][0]:
                    min_value = heapq.heappop(min_heap[0])
                    heapq.heappop(min_heap[1])
                # heapq.heappush(min_heap[1], min_value)
                heapq.heappush(max_heap[1], - min_value)
            cnt-=1
    if cnt == 0:
        print('EMPTY')
    else:
        max_value = heapq.heappop(max_heap[0])
        while len(max_heap[1]) > 0 and max_value == max_heap[1][0]:
            max_value = heapq.heappop(max_heap[0])
            heapq.heappop(max_heap[1])
        min_value = heapq.heappop(min_heap[0])
        while len(min_heap[1]) > 0 and min_value == min_heap[1][0]:
            min_value = heapq.heappop(min_heap[0])
            heapq.heappop(min_heap[1])
        
        # print(-max_heap[0][0], min_heap[0][0])
        print(-max_value, min_value)
    # print(max_heap, min_heap)
    