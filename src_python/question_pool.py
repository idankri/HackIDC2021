from utils.singleton import Singleton


class QuestionPool(metaclass=Singleton):
    def __init__(self):
        self.m_pool = list()

    def get(self, question_num: int):
        return self.m_pool[question_num]