import sys
import collections
que = []
front = 0
rear = 0
order = []
answer = []

if __name__ == '__main__':
    case = int(sys.stdin.readline())

    for i in range(case):
        # n, m = map(int, sys.stdin.readline().split())
        # p = list(map(int, sys.stdin.readline().split()))
        n = 6
        m = 3 # 2->6번째 / 0 : 3->4번
        p = [3,3,5,2,4,3]

        tmp = [[p[i], i] for i in range(n)]
        # p_sort = sorted(tmp, reverse=True)
        # p_index = [i[1] for i in p_sort]

        order = [[0,0]]
        print(order)
        for i in range(n):
            for j in range(n):
                if tmp[i][0] > order[j][0]:
                    order.insert(j,tmp[i])
                    break
        order.pop()
        print(order)


        # if p.count(tmp[m][0]) == 1:
        #     print(order.index(m)+1)
        #
        # else:
        #     if m > p_index[0]:
        #
        #     print('yet')

