number = eval(input( "Enter a number : "))

N1 = number%10
remaining = number//10

N2 = remaining%10
remaining = remaining//10

N3 = remaining % 10
remaining = remaining //10

print("The sum of Digits are : ", N1+N2+N3)
