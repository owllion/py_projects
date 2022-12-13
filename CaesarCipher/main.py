from art import logo
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z'
]
#duplicating these letters solve the problem when there is "z" in the text passed by the user.(z's index can not be shifted,it would just cause error =>  index out of range. So by duplicating letters, index() method can find the new position.)

def caesar(start_text, shift_amount, cipher_direction):
    res = ""
    start_text = list(start_text)
    if cipher_direction == 'decode': shift_amount*=-1  
    for letter in start_text:
        # if letter.isalpha():
        #     newPos = alphabet.index(letter) + shift_amount
        #     res += alphabet[newPos]
        #     continue
        # res += letter
        #just determine if the letter is in the alphabet
        #and do the thing above, else += letter...
        if letter in alphabet:
            newPos = alphabet.index(letter) + shift_amount
            res += alphabet[newPos]
        else: res += letter
          
    # res = "".join(res)
    print(f"the {cipher_direction} text is {res}")

print(logo)

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Want to play again? Type yes or no.\n" )
  if result == 'no':
    should_continue = False
    print('GoodBye!')