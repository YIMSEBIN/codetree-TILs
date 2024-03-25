n = int(input())
nums = list(map(int, input().split()))

nums.sort()

print(nums[2*n-1]+nums[2*n-2])