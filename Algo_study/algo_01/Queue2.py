#https://codingdog.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-listpop0%EC%9D%84-%EC%93%B0%EB%A9%B4-%EC%95%88-%EB%90%98%EB%82%98%EC%9A%94

import sys
import collections
Que = collections.deque()
front = -1
rear = -1

def push(n):
    global rear
    Que.append(n)
    rear = rear+1
def pop():
    global rear
    if front == rear:
        print(-1)
    else :
        tmp = Que.popleft()
        rear = rear-1
        print(tmp)
def empty():
    if front == rear:
        print(1)
    else:
        print(0)

if __name__=='__main__':
    n = int(sys.stdin.readline())

    for i in range(n):
        command = sys.stdin.readline().split()
        if command[0] == 'push':
            push(command[1])
        elif command[0] == 'pop':
            pop()
        elif command[0] == 'size':
            print(len(Que))
        elif command[0] == 'empty':
            empty()
        elif command[0] == 'front':
            if rear == front:
                print(-1)
            else:
                print(Que[0])
        elif command[0] == 'back':
            if rear == front:
                print(-1)
            else:
                print(Que[rear])

