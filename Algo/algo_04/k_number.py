import sys


def cal(left, right):

    if left > right:
        #print('left = '+str(left))
        #print('right = ' + str(right))
        return left


    mid = (left + right) // 2
    cnt = 0

    print('--------mid={}----------'.format(mid))
    #print('-left = ' + str(left))
    #print('-right = ' + str(right))
    for i in range(1, n + 1):
        if mid//i >= n:
            print('count=' + str(n))
            cnt += n
        else:
            print('count=' + str(mid//i))
            cnt += mid // i

    print('total_cnt= ' +str(cnt))


    if cnt < k:
        return cal(mid+1,right)
    else:
        return cal(left, mid-1)

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    answer = cal(1, k)
    print(answer)




# 1 2 2 3 3 4 6 6 9
# 1 2 3
# 2 4 6
# 3 6 9

##k = 8
###start = 1
###end = 8
###mid = 4
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16


# 1 2 3 4 mid//i = 4
# 1 2 3 4 mid//i = 2
# 1 2 3 4 mid//i = 1
# 1 2 3 4 mid//i = 1

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25


#10 20 30 15 18 35 40

# 10 20 30 35 40
# 10 15 35 40

#10 20 30 20 50

# 10 20 30 50
#
