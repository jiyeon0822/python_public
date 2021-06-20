import sys

coin = []
cnt = []

# 1 2 5
# 1 - 1
# 2 - 1 1 - 1
#----
# 5
# 5-5 = 0(1)
# 5-2 = 3
# 3-2 = 1 cnt[1] = 1
# 5-3 = 2 cnt[2] = 1
# 5-1 = 4
# 4-1 = 3 cnt[1] = 1
# 1-1 = 0 (1)
1 1 1 1 1
1 1 1 2
2 2 1
5

5
1 4
4 - 1 1 1 1
4 - 2 2
4 - 2 1 1

2 - 1 1 (1*1)
2 - 2 (1)

1 - 1 (1)



def cal_money(m):

    for c in coin:
        print('coin'+str(c))
        if m-c == 0:
            print('same')
            cnt[m] = cnt[m] + 1
            print('***')
            print(cnt[m])
            return 1
        elif m-c > 0:
            print('>')
            cnt[m] += cal_money(m-c)
            print('***')
            print(cnt[m])
        else:
            print('minus')
            cnt[m] = 0
            print('***')
            print(cnt[m])
            return 0

    return cnt[m]
    print(cnt[m])

if __name__ == '__main__':

    # N, K = list(map(int, sys.stdin.readline().split()))
    #
    # for i in range(N):
    #     coin.append(int(sys.stdin.readline()))

    coin = [1,2]
    cnt = [0]*10

    a = cal_money(5)
    print('----final------')
    print(cnt[5])



