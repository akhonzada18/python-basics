a = eval(input("Enter 1st edge : "))
b = eval(input("Enter 2nd edge : "))
c = eval(input("Enter 3rd edge : "))

if a+b>c and b+c>a and a+c>b :
    print("perimeter of triangle is ", a+b+c)
else:
    print("invalid")