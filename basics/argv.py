#iterating over a list in Python
from sys import argv            #importing argv

if len(argv)==2:                #checking if there is an arguement provided after the filename (Second word the user types after the filename)
    print(f"Hello, {argv[1]}")
else:
    print("Hello, world!")    

#iterates over each element in the argv list
for arg in argv:
    print(arg)    