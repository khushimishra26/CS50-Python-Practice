#storing a value in a variable
counter=0
height=6

#string inputting
answer = input("What is your name? ")

#string concatenation
print("My name is " + answer)

#OR by using fstrings (or format-string, to replace whatever is within the curly braces)
print(f"My name is {answer}")

#conditionals
#if-else and elif (a python version of else-if used in C/C++)
if height%3==0 and height%2!=0:         #python reads and, or, not same as &&, ||, ! in logical statements
    print("Odd")
elif height%2==0:
    print("Even")   
else:
    print("NaN")    

#looping statements (only two in Python :p)
#while loop (Entry controlled loop)
i=3
while i!=0:
    print("Height not zero")    #prints this statement thrice
    i-=1

#for loop
for j in range(3,10,2):
    print("I am a for-loop")    #prints this statement thrice




