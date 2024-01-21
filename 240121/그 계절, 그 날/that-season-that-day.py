def func(y, m, d) :
    if m == 2 and d == 29 :
        print("here")
        print(y % 400)
        print(y % 4)
        print(y % 100)
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) :
            continue
        else :
            return -1
    if 3<= m <= 5 :
        return "Spring"
    elif 6<= m <= 8 :
        return "Summer"
    elif 9<= m <= 11 :
        return "Fall"
    else :
        return "winter"


y, m, d = map(int, input().split())
print(func(y, m, d))