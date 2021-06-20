import sys

if __name__ =='__main__':

    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))


    answer = []
    for i in numbers:
        left = 0
        right = len(numbers)
        while left <= right:
            mid = (left+right)//2






    print(len(answer))