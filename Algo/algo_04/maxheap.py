import sys
import heapq

if __name__ =='__main__':

    n = int(sys.stdin.readline())

    heap = []
    for i in range(n):
        m = int(sys.stdin.readline())
        if m == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(abs(heapq.heappop(heap)))
        else:
            heapq.heappush(heap, -m)