from data import question_data
import random
class Question():
    def __init__(self) -> None:
        pass
    def next_question(self):
        q=random.choice(question_data)
        return(q["text"],q["answer"])
