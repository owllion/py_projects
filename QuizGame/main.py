from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
#class and data

question_bank = []
for data in question_data:
    question = data["text"]
    answer = data["answer"]
    question_bank.append(Question(question,answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
#每次call next Q就會增加num，這個QuizBank實體的number
#也維持<len(list)->繼續執行

print("You've completed the quiz!")
print(f"Your total score is {quiz.score}/{len(question_bank)}")