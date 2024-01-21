def func(y, m, d) :
    if m == 2 and d == 29 :
        if (y%100 == 0 and y%400 != 0) or (y%4 != 0) :
            return -1
    if 3<= m <= 5 :
        return "Spring"
    elif 6<= m <= 8 :
        return "Summer"
    elif 9<= m <= 11 :
        return "Fall"
    else :
        return "Winter"


y, m, d = map(int, input().split())
print(func(y, m, d))