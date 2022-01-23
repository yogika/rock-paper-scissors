rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
print("______WELCOM TO THE ROCK, PAPER AND SCISSORE GAME______")
print("ROCK =",rock ,"PAPER = ",paper,"SCISSORS = ",scissors)
use_game_image=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
if user>=3 or user<0:
  print("invalid number")  
else:
  print(use_game_image[user])
  com=random.randint(0,2)
  print(f"computer chose:")
  print(use_game_image[com])
  if user==2 and com==0:
    print("you lose")
  elif user==0 and com==2:
    print("you win") 
  elif com==user:
    print("draw")
  elif com>user:
    print("you lose")  
  elif user>com:
    print("you win")  
