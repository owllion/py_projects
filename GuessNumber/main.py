
import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    
def playAgain():
  again = input("Do you want to play again? Type 'yes' or 'no'")
  if again : playGame()
    
def compare(target,guessed):
  if target == guessed: return f'You got it! The number is {target}'
  elif target > guessed: return 'l'
  else: return 'h'
  
def playGame():
  target = random.randint(1,100)
  print(logo)
  print("Welcome to the Number Guessing Game!\n")
  print("I'm thinkig of a number between 1 to 100\n")
  # difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
  # attemptTimes = 10 if difficulty == "easy" else 5
  attemptTimes = set_difficulty()
  
  while attemptTimes:
    print(f"You have {attemptTimes} attempts remaining to guess the number.\n")
    guessed = int(input("Make a guess:"))
    res = compare(target,guessed)
    if res == "l":
      print("Too low.\n Guess again.")
      attemptTimes-=1
    elif res == "h":
      print("Too high.\n Guess again.")
      attemptTimes-=1
    else: 
      print(res)
      playAgain()

  print(f'You lose. The number is {target}')
  playAgain()
    
playGame()