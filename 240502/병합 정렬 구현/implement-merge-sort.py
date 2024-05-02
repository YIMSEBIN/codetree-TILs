n = int(input())
nums = list(map(int, input().split()))

def merge_sort(low, high) :
    if low < high :
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid+1, high)
        merge(low, mid, high)

def merge(low, mid, high) :
    result = []
    a = low
    b = mid+1
    while a <= mid and b <= high :
        if nums[a] < nums[b] :
            result.append(nums[a])
            a += 1
        else :
            result.append(nums[b])
            b += 1
    while a <= mid :
        result.append(nums[a])
        a += 1
    while b <= high :
        result.append(nums[b])
        b += 1
    
    c = 0
    for i in range(low, high+1) :
        nums[i] = result[c]
        c+=1

merge_sort(0, n-1)
print(*nums)