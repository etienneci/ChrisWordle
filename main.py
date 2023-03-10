### Setup Section ###


from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, secret):
  
  # Loop through each index/position 
  for index in range(6):
    
    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in secret):
      
      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    
      print(Style.RESET_ALL + " ", end="")

# Function to get word from user
def getSixLetterInput():
  guess = input("Enter a 6 letter word: ")
  while len(guess) < 6 or len(guess) > 6:
    guess = input("Enter a 6 letter word: ")
  return guess

### Main Program ###

# Introduction
print(r"""     


 __       __                            __         ______                                              
/  |  _  /  |                          /  |       /      \                                             
$$ | / \ $$ |  ______    ______    ____$$ |      /$$$$$$  |  ______   _____  ____    ______    _______ 
$$ |/$  \$$ | /      \  /      \  /    $$ |      $$ | _$$/  /      \ /     \/    \  /      \  /       |
$$ /$$$  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$$ |      $$ |/    | $$$$$$  |$$$$$$ $$$$  |/$$$$$$  |/$$$$$$$/ 
$$ $$/$$ $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |      $$ |$$$$ | /    $$ |$$ | $$ | $$ |$$    $$ |$$      \ 
$$$$/  $$$$ |$$ \__$$ |$$ |      $$ \__$$ |      $$ \__$$ |/$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/  $$$$$$  |
$$$/    $$$ |$$    $$/ $$ |      $$    $$ |      $$    $$/ $$    $$ |$$ | $$ | $$ |$$       |/     $$/ 
$$/      $$/  $$$$$$/  $$/        $$$$$$$/        $$$$$$/   $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ $$$$$$$/  
                                                                                                       
                                                                                                                                                                                                    
  """)

print("Welcome to Word Games.")
print("_______________________________________________________________________________")
print()
print("You have five chances to guess the word")
print("The word is six characters long")
print("If the character is in the right spot, it will be green")
print("If it's not in the right spot, but is in the word, it will be yellow")
print("If it's not in the word at all, it will be red")
print()
print()
# Set the secret word, and take in guesses. Determine if guesses are correct or not.
secret = "iceman"
guesses = 0
for chances in range(5):
  guess = getSixLetterInput()
  printGuessAccuracy(guess, secret)
  if guess != secret:
    guesses += 1
  if guesses == 5:
    print("Sorry You Lose")
    break
  if guess == secret:
    print("Congrats")
    break
    
  
    
       
  
  