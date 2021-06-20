import collections
queue = collections.deque()
front = -1
rear = -1

def remove():
    global rear
    queue.popleft()
    rear = rear-1
def move():
    tmp = queue.popleft()
    queue.append(tmp)

if __name__ == '__main__':
    n = int(input())
    rear = n-1
    for i in range(n):
        queue.append(i + 1)

    while rear > 0:
        remove()
        move()

    print(queue.pop())
