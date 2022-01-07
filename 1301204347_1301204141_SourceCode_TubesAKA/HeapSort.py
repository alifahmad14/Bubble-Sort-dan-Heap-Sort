from heapq import heappush, heappop
import random
import time

def heapsort(data, drawData, timeTick):
    heap = []
    for i in data:
        heappush(heap, i)
    
    ordered = []
    while heap:
        ordered.append(heappop(heap))
        time.sleep(timeTick)
    
    return ordered
    drawData(data, ['green' for x in range(len(data))])

