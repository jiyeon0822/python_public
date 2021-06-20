import sys
sys.setrecursionlimit(10**6)
global array
global numbers

def cal(front, end):
    if array[front][end] == 9:
        if numbers[front] == numbers[end]:
            if end-front == 2 or end-front == 1:
                array[front][end] = 1
                return 1
            array[front][end] = cal(front+1, end-1)
            return array[front][end]
        else:
            array[front][end] = 0
            return 0
    else:
        return array[front][end]

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split(' ')))
    # N = 7
    # numbers = [1, 2, 1, 3, 1, 2, 1]
    array = [[9] * N for i in range(N)]

    M = int(sys.stdin.readline())
    for i in range(M):
        front, end = map(int, sys.stdin.readline().split(' '))

        if front == end:
            print(1)
        else:
            front = front - 1
            end = end - 1
            print(cal(front, end))


