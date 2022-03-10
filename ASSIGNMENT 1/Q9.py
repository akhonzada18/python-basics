num = eval(input("Enter a number : "))
condition_ = num
reverse = 0

while(num>0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    
if condition_ == reverse :
        print("Number is a palindrome")
        
else:
        print("NUmber is not a Plindrome")