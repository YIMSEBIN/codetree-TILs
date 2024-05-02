n = int(input())
nums = list(map(str, input().split()))
pos = 0
for i in nums :
    if pos < len(i) :
        pos = len(i)
for i in range(n) :
    while len(nums[i]) < pos :
        nums[i] = '0' + nums[i]

for i in range(pos-1, -1, -1) :    
    arr_new = [[] for _ in range(10)]
    for j in range(n) :
        arr_new[int(nums[j][i])].append(nums[j])
    store_arr = []
    for j in range(10) :
        if len(arr_new[j]) != 0 :
            store_arr += arr_new[j]
    nums = store_arr

for i in range(n) :
    while nums[i][0] == '0' :
        nums[i] = nums[i][1:]
print(*nums)