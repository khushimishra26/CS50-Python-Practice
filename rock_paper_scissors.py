#rock paper scissors - 
#scissors beat paper
#rock beats scissors
#paper beats rock
import random
def game():
  user=input("Enter choice. r for rock, p for paper, s for scissors. \n")

  computer=random.choice(['r','p','s'])

  if user == computer:
    return "It\'s a tie"
  if whos_winnin(user,computer):
    return "You won! :D"

  return "You lost :("  

def whos_winnin(user,computer):
  #results in true if player wins 
  #r>s, p>r, s>p
  if(user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
    return True

print(game())    
