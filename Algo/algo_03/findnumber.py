import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    q = list(map(int, sys.stdin.readline().split()))

    a.sort()
    print(a)

    for i in q:
        print('****input = {}' .format(i))
        result = 0
        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            print('left = {}, right ={}, mid = {}'.format(left, right, mid))
            print('mid value = {}' .format(a[mid]))
            if a[mid] < i:
                left = mid+1
            elif a[mid] > i:
                right = mid-1
            else:
                result = 1
                break
        print(result)


