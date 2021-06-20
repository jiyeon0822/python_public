import sys

if __name__ =='__main__':

    numbers = [2,7]

    # print(bin(3))
    # print(bin(7))
    #
    # print(bin(3 ^ 7))
    # print(bin(3 ^ 7).count('1'))

    #011111111111111111
    #100000000000000000
    #100000000000000001
    #100000000000000010


    for i in numbers:
        j = i+1
        while 1:
            if bin(i^j).count('1') <= 2:
                print(j)
                break
            j+=1



