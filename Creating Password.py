small = 0
cap = 0
number = 0
sp = 0
password = input("Enter a password:")
for i in password:
    ####ssmall check#####
    if i >= 'a' and i <= 'z':
        small = 1
    elif i >= 'A' and i <= 'Z':
        cap = 1
    elif i >= '0' and i <= '9':
        number = 1
    elif i == '$' or i == '#' or i == '@':
        sp = 1
if(len(password)<= 16 and len(password)>= 6 and small == 1 and cap == 1 and number == 1 and sp ==1):
    print("Password is valid")
else:
    print("Password is not valid")