#to find all the divisors for a number x, from 2 to x-1
def find_divisors(x):
  for i in range(2,x):
    if x%i==0:
      print(i)
find_divisors(20)         #can be any number to call and execute the function
