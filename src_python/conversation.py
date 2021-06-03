from UserData import UserData
from globals import *
from question_pool import main_question_pool


class Conversation:
    def __init__(self, user_id: str):
        self.m_user_data = UserData(user_id, "")
        self.m_cur_question = 0

    def process_message(self, message: str):
        try:
            self.m_cur_question = main_question_pool.get(
                self.m_cur_question).process_answer(message, self.m_user_data)
            yield main_question_pool.get(self.m_cur_question).get_message()
        except InvalidMessageError:
            yield main_question_pool.get(self.m_cur_question).get_invalid_message()

    def process_image(self, image_data):
        try:
            self.m_cur_question = main_question_pool.get(
                self.m_cur_question).process_image(image_data, self.m_user_data)
            return main_question_pool.get(self.m_cur_question).get_message()
        except InvalidMessageError:
            return main_question_pool.get(self.m_cur_question).get_invalid_message()