
import random ; 
from words import word_list
from stages import stages
lives = 6
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


chosen_word = random.choice(word_list)
temp = ["_"]*len(chosen_word)

print('Welcome\n')
print(logo)
print(f'Pssst, the solution is {chosen_word}.')
print(temp)

end = False

while not end : 
  guess = input("Guess a letter: ").lower()
  for key,val in  enumerate(chosen_word):
    if val == guess: 
      temp[key] = val
  print(''.join(temp))
      
  if "_" not in temp:
    print('You Win')
    end=True
    
  if guess not in chosen_word:
    print(stages[lives])
    print(f"your guess is {guess}, not in the target,lost a live ")
    lives-=1
    if lives == 0: 
      end = True
      print('Lose')
    