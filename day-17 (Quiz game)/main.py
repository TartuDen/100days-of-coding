from question_model import Question
from quiz_brain import Brain

question_count=1
true_count=0
stop_=False
new_question=Question()
next_=Brain()

while not stop_:
    for i in range(5):
        question=(new_question.next_question())

        answer=input(f"Q{question_count}: {question[0]}. (True/False)?: ")
        
        if answer.lower()==question[1].lower():
            print(f"You got it right!\nThe correct answer was {answer}")
            true_count+=1
        else:
            print(f"That's wrong... :(\nThe correct answer was {question[1]}")
        print(f"Your current score is: {next_.counter(true_count,question_count)}")
        question_count+=1
    print(f"That's the game! your final score is {next_.counter(true_count,question_count-1)}")
    ask_again=input("Would you like to play again? Y/N: ")
    if ask_again.lower()=="n":
        stop_=True
    else:
        question_count=1
        true_count=0
