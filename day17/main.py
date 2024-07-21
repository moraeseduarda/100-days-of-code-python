# The Quiz Project

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# TODO: 2. Write a for loop to iterate over the question_data.
# TODO: 3. Create a Question object from each entry in question_data.
# TODO: 4. Append each Question object to the question_bank.

for data in question_data:
    q_text = data["question"]
    q_answer = data["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}.")
