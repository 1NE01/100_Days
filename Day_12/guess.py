from random import randint
import random
from Day_12.art import logo
print(logo)
print("weclome to the game")
print("thinking between 1 to 100")
difficulty_level=input("Choose the diffculty Type easy or hard")
easy_level=10
hard_level=5
answer = random.randint(1,100)
print(answer)
if(difficulty_level=="easy"):
  while(easy_level > 0):
  
    print(f"No of attempts available {easy_level}")
    userchoice=int(input("guess the number"))
    if(userchoice==answer):
      print("you win")
      break
    elif(userchoice>answer):
      print("too high")
    else:
      print("too low")
    easy_level-=1
    if(easy_level==0):
      print(f"loseeeeeeeeeeeeeeeeeeeeeeee{answer}")
     
else:
  while(hard_level > 0):
  
    print(f"No of attempts available {hard_level}")
    userchoice=int(input("guess the number"))
    if(userchoice==answer):
      print("you win")
      break
    elif(userchoice>answer):
      print("too high")
    else:
      print("too low")
    hard_level-=1
    if(hard_level==0):
      print(f"loseeeeeeeeeeeeeeeeeeeeeeee{answer}")
  