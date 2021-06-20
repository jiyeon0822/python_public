import collections
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ans = []
temp = collections.deque()
max_value = ''

for i in range(n-1):
    if a[i] < a[i+1]:
        ans.append(a[i+1])
        max_value = a[i+1]
        while(temp):
            index = temp.popleft()
            if a[index] < max_value:
                ans[index] = max_value
            else:
                temp.append(index)
    else:
        ans.append(-1)
        temp.append(i)

ans.append(-1)
print(ans)

