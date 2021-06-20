import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    lines = [int(sys.stdin.readline()) for i in range(n)]

    min = min(lines)*n/m
    max = sum(lines)/m
    answer = min

    while min <= max:
        mid = (min + max + 1)//2

        cnt = 0
        for i in lines:
            cnt = cnt + i//mid

        if cnt < m:
            max = mid-1
        elif cnt >= m:
            min = mid+1
            answer = mid

    print(int(answer))