def quick_sort(low, high) :
    if low < high :
        pivot = partition(low, high)
        quick_sort(low, pivot-1)
        quick_sort(pivot+1, high)

def partition(low, high) :
    target = low-1
    pivot = nums[high]
    for cur in range(low, high) :
        if nums[cur] < pivot :
            target += 1
            nums[cur], nums[target] = nums[target], nums[cur]
    nums[target+1], nums[high] = nums[high], nums[target+1]
    return target+1

n = int(input())
nums = list(map(int, input().split()))
quick_sort(0, n-1)
print(*nums)