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

def heap_sort() :
    for i in range(n, -1, -1) :
        heapify(i, n-1)
    
    for i in range(n-1, 0, -1) :
        nums[0], nums[i] = nums[i], nums[0]
        heapify(0, i-1)

heap_sort()
print(*nums)