def foo(a, b) :
    ra, rb = 0, 0
    if a > b :
        ra = a*2
        rb = b+10
    else :
        ra = a+10
        rb = b*2
    
    return ra, rb

a, b = map(int, input().split())
ra, rb = foo(a, b)
print(ra, rb)