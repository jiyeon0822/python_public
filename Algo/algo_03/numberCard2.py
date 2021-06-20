import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cards = list(map(int,sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    quest = list(map(int,sys.stdin.readline().split()))

    cnt_list = {}
    for i in cards:
        try:
            cnt_list[i] = cnt_list[i] + 1
        except KeyError:
            cnt_list[i] = 1

    #dictionays are hash tables -> looking up a key is a amortized constant time operation
    for i in quest:
        try:
            print(cnt_list[i], end=' ')
        except KeyError:
            print(0, end=' ')


