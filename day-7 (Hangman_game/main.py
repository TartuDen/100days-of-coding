#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

rnd_word=random.choice(word_list)
list_answer=[]
for i in rnd_word:
  list_answer.append("")
print(list_answer)
  
num_of_guesses=int(len(rnd_word)*1.5)

while num_of_guesses:
  if len(''.join(list_answer))!=len(rnd_word):
    num_of_guesses-=1
    match=False
    guess=input("Please, guess a letter: ").lower()
    for idx, letter_ in enumerate(rnd_word):  
      
      if letter_ == guess:
        list_answer[idx]=guess
        match=True

    if match:
      print(f"Congrats! There is letter {guess}")
      print(list_answer)
      if num_of_guesses:
        print(f"you have left {num_of_guesses} gueeses")
      else:
        print("sorry, you ran out of guesses")
      print("----------------------------------------")
    else:
        print(f"sorry, no letter {guess} in this word, try again")
        if num_of_guesses:
          print(f"you have left {num_of_guesses} gueeses")
        else:
          print("Sorry, no more guesses for you!")
        print("-------------------------------")
  else:
    break

if len(''.join(list_answer)) !=len(rnd_word):
  print("you lost!")
else:
  print("You WON!!!")
