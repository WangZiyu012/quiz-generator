from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
def question_bank_init():
    for index in range(0, len(question_data)):
        data_now = question_data[index]
        data_now_text = data_now["text"]
        data_now_answer = data_now["answer"]
        question_now = Question(text=data_now_text, answer=data_now_answer)
        question_bank.append(question_now)


print("Hello, welcome to the quiz test!")

question_bank_init()

quiz = QuizBrain()

# for question_index in range(0, len(question_bank)):
#     question_now = question_bank[question_index]
#     user_wrong_count = 0
#     user_right_count = question_index - user_wrong_count -1
#     print(question_now["text"])
#     user_answer = input("True or False?")
#     if question_now["answer"] != user_answer:
#         user_wrong_count+=1
#         print("You are wrong!")
#     else:
#         user_right_count+=1
#         print("You are right!")
#     print(f"Your score now is {user_right_count}/{question_index}")
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.question()

























