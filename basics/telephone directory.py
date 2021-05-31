#implementation of keys and values (a phonebook) It uses a hash table, where a value is mapped against a key. It is pretty fast (a constant time complexity O(1)) to access thus efficient as a data structure
people={                                            #a dictionary, with keys against which values are mapped
    "John": "+91-8739274234",
    "Jane": "+91-7482748274"
}
name=input("Enter name whose number is to be searched: ")
if name in people:                                  #only names are searched, if a match is found, then the value is accessed
    print(f"The number is :{people[name]}")         #name variable can act as an indexing value for movement in the phonebook
else:
    print("Not found")    