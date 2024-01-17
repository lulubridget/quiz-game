from question_model import Question
from game_data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question ["text"]
    question_answer = question ["answer"]
    next_question = Question(text=question_text, answer=question_answer)
    question_bank.append(next_question)

quiz = QuizBrain(question_list=question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You complete the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")