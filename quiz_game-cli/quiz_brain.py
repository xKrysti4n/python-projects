class QuizBrain:
    def __init__(self,q_bank):
        self.score = 0
        self.question_number = 0
        self.question_list = q_bank
    def next_question(self):
        current_question = self.question_list[self.question_number]
        useranswer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)?: ").capitalize()
        self.question_number+=1
        self.check_answer(useranswer,current_question.answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def check_answer(self,userans,currentans):
        if userans == currentans:
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
            print(f"The correct answer is: {currentans}")
        print(f"Your current score is: {self.score}/{self.question_number}")

