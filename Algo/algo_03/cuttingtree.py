import sys


def cal(trees, mid_h):
    total = 0
    for t in trees:
        if t > mid_h:
            total += t - mid_h
        else:
            break
    return total


if __name__ == '__main__':
    # n, m = map(int, sys.stdin.readline().split())
    # trees = list(map(int, sys.stdin.readline().split()))

    n = 4
    m = 7
    trees = [20,15,10,17]

    trees.sort(reverse=True)

    max_h = trees[0]-1
    min_h = max_h - m
    answer = min_h

    while min_h <= max_h:
        mid_h = (min_h + max_h) // 2
        total = cal(trees, mid_h)

        if total < m:
            max_h = mid_h - 1
        else:
            answer = mid_h
            min_h = mid_h + 1


    print(answer)



