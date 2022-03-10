W = eval(input("Enter amount of water in KG :"))
I = eval(input("Enter initial temperature : "))
F = eval(input("Enter final temperature : "))

Q = W * (F - I) * 4184

print("THe Energy needed is : ",Q)