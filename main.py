# TextFunctions file contains functions that make text bold, italic, dim, changes color, etc.
import TextFunctions
import sys
import os

# Clearing the screen (just to be safe)
os.system('cls||clear')

while True:
  print(TextFunctions.dim_text("  _   _                                         "))
  print(TextFunctions.dim_text(" | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  "))
  print(TextFunctions.dim_text(" | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ "))
  print(TextFunctions.dim_text(" |  _  | (_| | | | | (_| | | | | | | (_| | | | |"))
  print(TextFunctions.dim_text(" |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|"))
  print(TextFunctions.dim_text("                    |___/                       "))
  
  print()
  
  print(TextFunctions.yellow_text("Welcome to Hangman."))
  print(TextFunctions.yellow_text("This is a two player game in which the first player enters a word and the second player guesses it."))
  print(
      TextFunctions.cyan_text(
          TextFunctions.bold_text(
              "Important note: If you finished guessing the word, type \"finished\" when asked to enter a letter"
          )))
  player1 = input("Enter the name of the first player: ")
  player2 = input("Enter the name of the guessing player: ")

  # Only if name is not blank, go to the next oart of the code.
  if (len(player1) and len(player2)) != 0:
    print()
    break
  else:
    print()
    print(
        TextFunctions.cyan_text(
            TextFunctions.bold_text("Sorry, name cannot be blank.")))
    print()
    continue

# Asking the player1 to enter a word for player2 to guess.
print(TextFunctions.dim_text(f"Hello {player1}! Please enter a word:"))

# Continually ask player1 to input a word for player2 to guess.
while True:
  word = input("Enter a word: ")

  # Quit the loop only if player1 has entered a word with no space and length of word is greater than 2.
  if len(word) <= 2:
    print(TextFunctions.red_text("Word has to be three letters or more."))
    continue
  elif word.lower() == "finished":
    print(
        TextFunctions.red_text(
            TextFunctions.bold_text(
                "Please choose any another word except the word 'finished'!")))
    continue
  elif (len(word) > 2) and (word.isspace() == False):
    print()
    print()
    break

# Creating a list called 'letters' that stores individual characters of variable 'word'
# as individual elements in the string. The strip() function serves that purpose.
letters = list(word.strip(""))

# This list is for printing the progress made by the player so far.
guessed_letters_for_printing = []

# Number of guesses player2 gets to guess the word
number_of_guesses = 8

print(TextFunctions.dim_text(f"Hello {player2}! Please guess a letter: "))

for x in range(number_of_guesses):
  # Do not print a new line on the first iteration.
  # Only if iteration is not the first, print a new line.
  if x > 0:
    print()

  guess = input("Enter a letter: ")

  # Only if player2 has typed finished, ask for the final word.
  if guess == "finished":
    guess_word = input("Enter the final word: ")
    if guess_word == word:
      print()
      print(
          TextFunctions.green_text(
              TextFunctions.italic_text(
                  "Congratulations, you beat the game!")))
      play_again = input("Do you want to play again [Y/N]?\n[Y/N]: ")
      if (play_again == 'Y') or (play_again == 'y'):
        # Clearing everything that was outputted for a fresh terminal
        os.system('cls||clear')

        # Restarting the program
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
      print()
      print(TextFunctions.red_text("Sorry, you lost."))
    exit()
  # Reject if the typed input is a space, is nothing or is a string with length greater than 1.
  elif (len(guess) == 0) or (guess.isspace() == True) or (len(guess) > 1):
    print(
        TextFunctions.cyan_text(
            TextFunctions.italic_text(TextFunctions.bold_text("Invalid!"))))
    continue
  else:
    if guess in letters:
      print(TextFunctions.green_text("You guessed the right letter!"))
      guessed_letters_for_printing.append(guess)
    else:
      print(
          TextFunctions.bold_text(
              TextFunctions.blue_text(
                  "The letter you guessed is not in the word!")))
  print(TextFunctions.yellow_text(
      TextFunctions.bold_text("Progress so far: ")),
        end='')

  # Printing the guessed letters.
  for x in word:
    if x in guessed_letters_for_printing:
      print(x, end='')
    else:
      print(" _", end='')
  print()
  print(
      TextFunctions.dim_text(
          f"You have {number_of_guesses - 1} guesses remaining!"))
  number_of_guesses -= 1

print()
print(
    TextFunctions.red_text(
        TextFunctions.bold_text(TextFunctions.italic_text("You lost!"))))
print(TextFunctions.magenta_text(f"The word was: {word}"))
