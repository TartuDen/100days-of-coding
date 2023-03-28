from vocab import words
import random

words_var=["eat","sleep","walk", "buss","car", "aircraft","moon","sun","san"]
w_keys=[]
for i

first_w=random.choice(words_var)
word_check=[]
print(f"First word is: {first_w}")
word_check.append(first_w)

for i in range(1,7):
    last_letter=word_check[-1][-1]
    print(last_letter)
    if i%2!=0:
        for w in words_var:
            if w[0] == last_letter and w not in word_check:
                print(f"Computer's move: word {w}")
                print(word_check[-1],"|",w)


