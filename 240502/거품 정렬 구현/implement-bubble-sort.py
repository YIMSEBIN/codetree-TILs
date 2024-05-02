n = int(input())
nums = list(map(int, input().split()))
flag = False
while not flag :
    flag = True
    for i in range(n-1) :
        if nums[i] > nums[i+1] :
            nums[i], nums[i+1] = nums[i+1], nums[i]
            flag = False

print(*nums)