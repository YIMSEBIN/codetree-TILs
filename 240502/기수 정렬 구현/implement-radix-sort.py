n = int(input())
nums = list(map(str, input().split()))
pos = 0
for i in nums :
    if pos < len(i) :
        pos = len(i)

for i in range(pos) :
    arr_new = [[] for _ in range(10)]
    for j in range(n) :
        arr_new[int(nums[j][pos-1])] = nums[j]
    store_arr = []
    for j in range(10) :
        store_arr += arr_new[j]
    nums = store_arr

print(*nums)