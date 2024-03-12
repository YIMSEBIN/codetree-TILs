def foo(a, b) :
    small, big = 0, 0
    if a > b :
        small = b
        big = a
    else :
        small = a
        big = b
    
    return small+10, big*2

a, b = map(int, input().split())
ra, rb = foo(a, b)
print(ra, rb)