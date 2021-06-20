import sys
import collections

Queue = collections.deque()

def find(num):
    idx = Queue.index(num)
    if idx <= len(Queue)-idx:
        mov = -idx
        Queue.rotate(mov)
        Queue.popleft()
        return idx
    else:
        mov = len(Queue) - idx
        Queue.rotate(mov)
        Queue.popleft()
        return mov


if __name__ == '__main__':

    N, m = map(int, sys.stdin.readline().split())
    order = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        Queue.append(i+1)

    answer = 0
    for j in range(m):
        answer = answer + find(order[j])

    print(answer)