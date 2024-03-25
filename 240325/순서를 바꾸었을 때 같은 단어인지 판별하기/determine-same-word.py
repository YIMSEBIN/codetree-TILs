a_str = input()
b_str = input()

a_str = ''.join(sorted(a_str))
b_str = ''.join(sorted(b_str))

if a_str == b_str :
    print("Yes")
else :
    print("No")