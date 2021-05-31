#working on string, lowercase uppercase demos
s=input("Before: ")
if(s.islower()):
    print("After: "+s.upper())

#OR use a for loop.. to iterate over individual characters in a string

elif(s.isupper()):
    print("After: "+s.lower())
else:
    print("Not a string!")        