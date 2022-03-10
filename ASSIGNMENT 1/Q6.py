x = eval(input("Enter 1st No. : "))
y = eval(input("Enter 2nd No. : "))
z = eval(input("Enter 3rd No. : "))

if x<y and x<z :
    if y<z :
        print(x,y,z)
    else:
        print(x,z,y)
elif y<x and y<z :
    if x<z :
        print(y,x,z)
    else:
        print(y,z,x)
elif z<x and z<y :
    if x<y :
        print(z,x,y)
    else:
        print(z,y,x)
        