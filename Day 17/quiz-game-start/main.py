# from data import question_data
# from question_model import Question
# from quiz_brain import *
#
# def main():
#     question_bank = []
#
#     for q in question_data:
#         question = Question(txt=q["text"], answer=q["answer"])
#         question_bank.append(question)
#
#     # for question in question_bank:
#     #     print(question.txt, question.answer)
#
#  quiz = QuizBrain(question_bank)
#     while quiz.still_has_questions():
#         quiz.next_question()
#
#     print('You have completed the quiz')
#     print(f'Your final score was: {quiz.score}/{len(question_bank)}')
#
# main()


from question_model import Question
from quiz_brain import *
from data import question_data


def main():

    question_bank = []
    for q in question_data:
        question_bank.append(Question(txt=q['text'], answer=q['answer']))

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print('You have completed the quiz')
    print(f'Your final score was: {quiz.score}/{len(question_bank)}')


main()