from data import question_data
from question_model import QuestionBank
from quiz_brain import QuizBrain as qb


my_qb = QuestionBank(question_data)
question_bank = []
for x in question_data:
    question = x["text"]
    answer = x["answer"]
    question_bank.append([question, answer])

input = True
while input:
    x = qb.next_question(question_bank)


