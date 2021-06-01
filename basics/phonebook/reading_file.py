#reading a file
file=open("phonebook.csv","r")
if file.mode=="r":
    #using read() to read files
    contents=file.read()
    print(contents)  
