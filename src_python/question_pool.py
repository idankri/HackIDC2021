from question import Question
from utils.singleton import Singleton


class QuestionPool(metaclass=Singleton):
    def __init__(self):
        self.m_pool = list()
        user_message = "אהלן אהלן! ביטוח עושים בווטצאפ! איפה גרים? דירה או בית פרטי?"
        error_message = "מתנצל לא הבנתי :( דירה או בית פרטי?"
        question_1 = Question('Property Type', user_message, error_message,
                              self.validation_function, self.get_next_question_id, True, False)
        self.m_pool.append(question_1)

    def get(self, question_num: int):
        return self.m_pool[question_num]

    @staticmethod
    def validation_function(user_msg):
        return user_msg == "דירה" or user_msg == "בית פרטי"

    @staticmethod
    def get_next_question_id(user_msg):
        return 1
