import collections
import sys
queue = collections.deque()
answer = []
front = 0
rear = 0

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    for i in range(n):
        queue.append(i+1)
    rear = n
    while front < rear:
        queue.rotate(-k+1)
        answer.append(queue.popleft())
        rear = rear-1

    print(str(answer).replace('[','<').replace(']','>'))
