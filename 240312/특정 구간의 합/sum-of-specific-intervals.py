n, m = map(int, input().split())
numlist = list(map(int, input().split()))
result = []
for i in range(m) :
    a, b = map(int, input().split())
    tmp = 0
    for i in range(a, b+1) :
        tmp += numlist[i-1]
    result.append(tmp)

for i in result :
    print(i)