n = int(input())
nums = list(map(int, input().split()))

def heapify(a, l) :
    cur_max_index = a
    if 2*a <= l and nums[cur_max_index] < nums[2*a] :
        cur_max_index = 2*a
    if 2*a+1 <= l and nums[cur_max_index] < nums[2*a+1] :
        cur_max_index = 2*a+1
    
    if a != cur_max_index :
        nums[cur_max_index], nums[a] = nums[a], nums[cur_max_index]
        heapify(cur_max_index, l)

def heap_sort(l) :
    for i in range(l, -1, -1) :
        heapify(i, l)
    nums[0], nums[l] = nums[l], nums[0]
    if l > 0 :
        heap_sort(l-1)

heap_sort(n-1)
print(*nums)