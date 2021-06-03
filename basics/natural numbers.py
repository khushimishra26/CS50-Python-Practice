#printing natural numbers from 1 to a number given in the argument of a function. Demo of a simple function.
def print_numbers_to(number):   #defining the function with name print_numbers_to, here, number is a formal argument
  for i in range(1,number+1):   #doing the required task
    print(i)
    
print_numbers_to(50)            #calling the function, with a value (50 here is an actual argument. Incase of a default argument, sending a value in the actual argument becomes optional)
