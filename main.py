from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

print(question_bank)

for i in range(0, len(question_bank)):
    print(question_bank[i].text, question_bank[i].answer)
