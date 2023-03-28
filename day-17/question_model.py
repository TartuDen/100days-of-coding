from data import question_data
import random
class Question():
    def __init__(self) -> None:
        pass
    def next_question(self):
        q=random.choice(question_data)
        # for l in len(question_data):
        #     yield(question_data["text"],question_data["answer"])
        return(q["text"],q["answer"])
