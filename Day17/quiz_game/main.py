from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# loop through the question data and create a question bank consisting
question_bank = []
for entry in question_data:
    question = Question(entry['question'], entry['correct_answer'])
    question_bank.append(question)

#create the question list by initiating a quizbrain object
quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print(f"The quiz is now complete. Final score: {quiz.score}/{quiz.question_number}")



