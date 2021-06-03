from question import Question
from utils.singleton import Singleton


class QuestionPool(metaclass=Singleton):
    def __init__(self):
        self.m_pool = list()

    def get(self, question_num: int):
        return self.m_pool[question_num]

    def add(self, question: Question):
        self.m_pool.append(question)


main_question_pool = QuestionPool()

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="",
    invalid_message=None,
    answer_validation_function=lambda user_msg: True,
    get_next_question_id=lambda user_msg: 1,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="אהלן אהלן כאן משה הסוקר",
    invalid_message=None,
    answer_validation_function=None,
    get_next_question_id=lambda user_msg: 2,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="שמח שבחרת בביטוח ישיר 😃 אשמח לשאול אותך כמה שאלות ולתת לך הצעת ביטוח בקלות ובמהירות!",
    invalid_message=None,
    answer_validation_function=None,
    get_next_question_id=lambda user_msg: 3,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="קודם כל עם מי יש לי את הכבוד לדבר?",
    invalid_message=None,
    answer_validation_function=lambda user_msg: not user_msg.isdigit(),
    get_next_question_id=lambda user_msg: 4,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="היי נעים להכיר!",
    invalid_message=None,
    answer_validation_function=None,
    get_next_question_id=lambda user_msg: 5,
    answer_flag=True,
    image_flag=False
))