

class QuestionBank:
    def __init__(self, question_text, question_answer):
        self.question = question_text
        self.answer = question_answer


    def question_bank(self, question):
        x = question.keys()
        y = question.values()
        return x,y