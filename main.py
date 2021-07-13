import random
colors=['blue','red','black','white','yellow','green','orange']
animals=['cat','dog','whale','giraffe','elephant','sloth','hedgehog']
print("This is password picker!")
color=str(random.choice(colors))
animal=str(random.choice(animals))
no=str(random.randrange(0,100))
print("Your new password is: ",color+animal+no)
#randrange() gives a range of numbers to randomly choose from.