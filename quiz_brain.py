# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

from question_model import Question
from data import question_data
from data import question_bank
class QuizBrain:
    def __init__(self, question_index, question_bank = question_bank):
    def ask(self):

    def check_correct(self):

    def check_end(self):


    pass


for question_index in range(0, len(question_bank)):
    question_now = question_bank[question_index]
    user_wrong_count = 0
    user_right_count = question_index - user_wrong_count -1
    print(question_now["text"])
    user_answer = input("True or False?")
    if question_now["answer"] != user_answer:
        user_wrong_count+=1
        print("You are wrong!")
    else:
        user_right_count+=1
        print("You are right!")
    print(f"Your score now is {user_right_count}/{question_index}")
