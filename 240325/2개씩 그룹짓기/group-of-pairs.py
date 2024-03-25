n = int(input())
nums = list(map(int, input().split()))

nums.sort()

print(nums[n-1]+nums[n-2])