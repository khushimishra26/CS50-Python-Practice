#declaring a list and performing a linear search on it
x=int(input("How many names in the list? "))
names=[]
for i in range(x):
    names.append(input("Enter name: "))
query=input("Enter name to be searched: ")
if query in names:
    print("Found")
else:
    print("Not found")    