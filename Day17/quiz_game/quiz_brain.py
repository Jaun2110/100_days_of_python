class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False):").lower()
        self.check_answer(user_answer, current_question.answer)
        self.display_score()

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"You are right!\nThe correct answer is {correct_answer}")
            self.score += 1
        else:
            print(f"That is wrong!\nThe correct answer is {correct_answer}")

    def display_score(self):
        print(f"You're score is {self.score}/{self.question_number}")


