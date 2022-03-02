class QuizBrain:
    def __init__(self, question_list):
        self.question_nr = 0
        self.question_list = question_list


    def next_question(self, question_nr, question_list):
        for question_nr in question_list:
            current_question = self.question_list[self.question_nr]
            user_answer = input(f"{self.question_nr} : {current_question.text} (True or False)")






