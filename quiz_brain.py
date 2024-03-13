# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

from question_model import Question
from data import question_data
from data import question_bank
class QuizBrain:
    def __init__(self, question_list, question_index, user_wrong_count):
        self.question_list = question_list
        self.question_index = question_index
        self.question_now = question_list[question_index]
        self.user_wrong_count = user_wrong_count
        self.user_right_count = question_index - user_wrong_count - 1
    def question(self):
        print(self.question_now["text"])
        self.user_answer = input("True or False?")

    def still_has_questions(self):
        while self.question_index < len(question_bank):
            return True
        else:
            return False

    def check_correct(self):
        if self.question_now["answer"] != self.user_answer:
            += 1
            print("You are wrong!")
        else:
            self.user_right_count += 1
            print("You are right!")
        print(f"Your score now is {self.user_right_count}/{self.question_index}")

    def check_end(self):
        len(question_bank)

    pass



    print(question_now["text"])
    user_answer = input("True or False?")
    if question_now["answer"] != user_answer:
        +=1
        print("You are wrong!")
    else:
        user_right_count+=1
        print("You are right!")
    print(f"Your score now is {user_right_count}/{question_index}")

