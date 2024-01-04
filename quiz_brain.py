class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            print("You are right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {answer}")
        print(f"Your score is {self.score}/{self.question_number}")
