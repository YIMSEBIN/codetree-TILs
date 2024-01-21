n, m = map(int, input().split())
big_number = n if n > m else m
for i in range(big_number, n*m+1) :
    if i % n == 0 and i % m == 0 :
        print(i)
        break