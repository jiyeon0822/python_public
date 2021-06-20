import sys

order = [[0,0]]*10
print(order)
p=[5,3,3,1,5]

index = [[p[i], i] for i in range(5)]
print(index)
index.sort(reverse=True)
p_index = [i[1] for i in index]

print(index)
print(p_index)