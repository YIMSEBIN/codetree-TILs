def func(a, b, c) :
    min = 101
    if a < min :
        min = a
    if b < min :
        min = b
    if c < min :
        min = c
    return min

a, b, c = map(int, input().split())
print(func(a, b, c))