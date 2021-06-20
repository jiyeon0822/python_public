import sys
import collections


if __name__ == '__main__':

    T = int(sys.stdin.readline())

    for i in range(T):
        p = list(sys.stdin.readline().replace('RR', "").rstrip())
        n = int(sys.stdin.readline())
        if n > 0:
            queue = collections.deque(map(int, sys.stdin.readline().lstrip('[').rstrip(']\n').split(',')))
        else:
            input()
            queue = collections.deque()

        if p.count('D') > n:
            print('error')
            continue

        flag = 1
        for func in p:
            if func == 'R':
                flag = flag * -1
            else:
                if flag == 1:
                    queue.popleft()
                else:
                    queue.pop()

        if flag == -1:
            queue.reverse()

        print(str(list(queue)).replace(" ", ""))



