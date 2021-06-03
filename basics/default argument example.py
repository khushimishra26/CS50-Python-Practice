#function to return area of a cone, here, demo for default argument is shown. 
#In Python, the name of the argument is to be explicitly mentioned while passing values in the actual argument (only to be done, when a default value is to be used for computation)
def calculate_cone_area(r=1, pi=3.14, h=1):
  return (1.0/3) * pi * r * r * h
calculate_cone_area(r=5,h=3)          #only r and h are required, thus, mentioned.
