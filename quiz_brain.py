# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

from question_model import Question
from data import question_data
class QuizBrain:
    def __init__(self, question_list ):
        self.question_list = question_list
        self.question_index = 0
        self.score = 0
        self.question_now = question_list[self.question_index]

    def question(self):
        self.question_index += 1
        print(self.question_now["text"])
        user_answer = input("True or False?")
        correct_answer = self.question_now["answer"]
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_index < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if self.question_now["answer"] != user_answer:
            self.score+= 1
            print("You are wrong!")
        else:
            self.score += 1
            print("You are right!")
        print(f"Your score now is {self.score}/{self.}")

