a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
#performing addition
print(a+b)
#performing division (with precision)
print(a/b)
#performing division (sans precision)
print(a//b)
#obtaining remainder
print(a%b)
#performing multiplication
print(a*b)
#performing subtraction
print(a-b)
#obtaining power of a number (a to the power b)
print(a**b)
#eg of a list of values
i=a+b
if i in ["0","1","2"]:
    print("First three")
else:
    print("OK!")     