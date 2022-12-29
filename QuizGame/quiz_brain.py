class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}  {current_question} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,current_answer):
        if user_answer == current_answer:
            self.score += 1
            print("You are right!")
            print(f"Current Score: {self.score}")
        else:
            print("Wrong answer.")
        print(f"Answer is {current_answer}/{self.question_number}")
        print("\n")
        #blank space between the questions.