import csv
from os import write
file = open("phonebook.csv","a+")        #creating a csv file named phonebook
name = input("Enter the name: ")
number = input("Enter the contact number: ")
writer = csv.writer(file)                 #wrap the file with csv functionality
writer.writerow([name,number])            #writing data in file
file.close()                              #closing file
