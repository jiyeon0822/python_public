numbers = [1,1,1,1,1]
target = 3
temp = []



for i in range(len(numbers)):
    print(i)
    if i == 0:
        temp.append(numbers[i])
        temp.append(-numbers[i])
    else:
        for j in range(len(temp)):
            temp.append(temp[j] + numbers[i])
            temp[j] = temp[j]-numbers[i]


print(temp)
answer=temp.count(target)
print(answer)