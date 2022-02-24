from data import question_data
from question_model import QuestionBank


my_qb = QuestionBank(question_data)

for x in question_data:
    print(my_qb.question_bank(x))

