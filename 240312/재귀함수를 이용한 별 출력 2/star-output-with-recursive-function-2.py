def foo(a, b, c) :
    if b == 2*c :
        return
    print(a*"* ")
    b = b + 1
    if b < c :
        foo(a-1, b, c)
    elif b == c :
        foo(a, b, c)
    else :
        foo(a+1, b, c)

n = int(input())
foo(n, 0, n)