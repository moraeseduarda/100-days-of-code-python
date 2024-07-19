# TODO: 5. Create a class called QuizBrain
# TODO: 6. Write an __init__() method.
# TODO: 7. Initialise the question_number to 0
# TODO: 8. Initialise the question_list to an input.
# TODO: 9. Retrieve the item at the current question_number from the question_list.
# TODO: 10. Use the input() function to show the user the Question text and ask the user's answer.
# TODO: 11. Create method called still_has_questions().
# TODO: 12. Return a boolean depending on the value of question_number.
# TODO: 13. Use a while loop to show the next question until the end.
# TODO: 14. Add a new attribute called score to the QuizBrain class and
#  increment it by one every time the user gets it right.


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
