import sys

def min_cal(rocks,distance):

    diff = []
    for i in range(len(rocks)):
        if i == 0:
            diff.append(rocks[0])
        else:
            diff.append(rocks[i] - rocks[i-1])
    diff.append(distance - rocks[-1])

    return min(rocks)

if __name__ =='__main__':

    distance = 25
    rocks = [2,14,11,21,17]
    n = 2

    rocks.sort()
    print(rocks)

    answer = 0
    for i in range(len(rocks)):
        sample = rocks
        sample.pop(i)
        print(sample)
        # for j in range(len(rocks)-1):
        #     sample2 = sample
        #     sample2.pop(j)
        #     cal = min_cal(sample2, distance)
        #
        #     if answer < cal:
        #         answer = cal

    #print(answer)
















