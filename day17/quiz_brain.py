# TODO: asking the questions.
# TODO: checking if the answer is correct.
# TODO: checking if we're the end of the quiz.

class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    # def still_has_question(self):
        # return true or false

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
