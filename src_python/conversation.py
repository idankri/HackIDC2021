from globals import *


# TODO: uncomment after merge
# from user_data import UserData


class Conversation:
    def __init__(self):
        # TODO: uncomment after merge
        # self.m_user_data = UserData()
        self.m_user_data = None
        self.m_cur_question = 0

    def process_message(self, message: str):
        try:
            self.m_cur_question = main_question_pool.get(
                self.m_cur_question).process_answer(message, self.m_user_data)
            return main_question_pool.get(self.m_cur_question).get_message()
        except InvalidMessageError:
            return main_question_pool.get(self.m_cur_question).get_invalid_message()

    def process_image(self, image_data):
        try:
            self.n_cur_question = main_question_pool.get(
                self.m_cur_question).process_image(image_data, self.m_user_data)
            return main_question_pool.get(self.m_cur_question).get_message()
        except InvalidMessageError:
            return main_question_pool.get(self.m_cur_question).get_invalid_message()