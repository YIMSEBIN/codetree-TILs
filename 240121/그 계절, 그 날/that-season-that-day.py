def func(y, m, d) :
    if m == 1 :
        if d > 31 :
            return -1
        else :
            return "Winter"
    elif m == 2 :
        if d == 29 and ((y%100 == 0 and y%400 != 0) or (y%4 != 0)) :
            return -1
        if d > 29 :
            return -1
        else :
            return "Winter"
    elif m == 3 :
        if d > 31 :
            return -1
        else :
            return "Spring"
    elif m == 4 :
        if d > 30 :
            return -1
        else :
            return "Spring"
    elif m == 5 :
        if d > 31 :
            return -1
        else :
            return "Spring"
    elif m == 6 :
        if d > 30 :
            return -1
        else :
            return "Summer"
    elif m == 7 and m == 8 :
        if d > 31 :
            return -1
        else :
            return "Summer"
    elif m == 9 :
        if d > 30 :
            return -1
        else :
            return "Fall"
    elif m == 10 :
        if d > 31 :
            return -1
        else :
            return "Fall"
    elif m == 11 :
        if d > 30 :
            return -1
        else :
            return "Fall"
    elif m == 12 :
        if d > 31 :
            return -1
        else :
            return "Winter"


y, m, d = map(int, input().split())
print(func(y, m, d))