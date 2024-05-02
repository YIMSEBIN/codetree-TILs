n = int(input())
nums = list(map(int, input().split()))

for i in range(1, n) :
    j = i-1
    key = nums[i]
    while j >= 0 and nums[j] > key :
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key

print(*nums)