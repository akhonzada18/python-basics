import math
x2 = eval(input("x2 = "))
y2 = eval(input("y2 = "))

x1 = 0
y1 = 0

p = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if p<=10:
    print("Point is inside the circle.")
else:
    print("Point is outside the circle.")