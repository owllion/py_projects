import random
from game_data import data
from art import logo, vs
from replit import clear


#get random account
def getRandomAccount():
  return random.choice(data)


#format data to print
def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name},a {description}, from {country}"
  
#check answer
def check_answer(guess,a_followers,b_follwers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
  #a wins -> if guess == "a", then return True，otherwise False
  if a_followers > b_follwers: return guess == "a" 
  return guess == "b"
  

def play_game():
  print(logo)
  score = 0
  should_conti = True
  b_play = getRandomAccount()
  while should_conti:
    #need to make data_player at position B become the next account at position A(就是位置會一直往前推一個)
    a_play = b_play
    #but b_play here will get the error coz b_play doesn't exist yet
    #so we have to declare it ahead this loop
    b_play = getRandomAccount()
    
    while a_play == b_play: a_play = getRandomAccount()
    #python可以直接obj 和 obj比對
      
    print(f"Compare A:{ format_data(a_play)}")
    print(vs)
    print(f"Against B:{ format_data(b_play)}")
  
    #make a guess
    guess = input("Which one has more followers? Type 'A' or 'B'").lower()
    isCorrect = check_answer(guess,a_play["follower_count"],b_play["follower_count"])
    clear()
    #new turn,need to clear the previous run's contents
    print(logo)
    if isCorrect: 
      score+=1
      print(f"You got it! The score is {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      should_conti = False
#check if followers number is the same -> True then get another account else do nothing
#check answer -> correct then go on else lose and show user's scores abd shoud_continue = False.

play_game()
