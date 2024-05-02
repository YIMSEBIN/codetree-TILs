n = int(input())
nums = list(map(str, input().split()))
pos = 0
for i in nums :
    if pos < len(i) :
        pos = len(i)

for i in range(pos) :
    for j in range(n) :
        if len(nums[j]) < i+1 :
            nums[j] = 0 + nums[j]
    arr_new = [[] for _ in range(10)]
    for j in range(n) :
        arr_new[int(nums[j][i])] = nums[j]
    store_arr = []
    for j in range(10) :
        store_arr += arr_new[j]
    nums = store_arr

print(*nums)