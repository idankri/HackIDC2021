from globals import *


class Question:
    def __init__(self, type_of_item, message_to_user, invalid_message, answer_validation_function, get_next_question_id,
                 answer_flag, image_flag):
        self.type = type_of_item
        self.message_to_user = message_to_user
        self.invalid_message = invalid_message
        self.answer_validation_function = answer_validation_function
        self.get_next_question_id = get_next_question_id
        self.answer_flag = answer_flag
        self.image_flag = image_flag

    def process_answer(self, user_answer : str, user_data) -> int:
        if not self.answer_flag or not self.answer_validation_function():
            raise InvalidMessageError()
        self.update_user_data(user_answer, user_data)
        return self.get_next_question_id(user_answer)

    def process_image(self, user_image):
        if not self.image_flag:
            raise InvalidMessageError()

    def get_message(self) -> str:
        return self.message_to_user

    def get_invalid_message(self) -> str:
        return self.invalid_message

    def update_user_data(self, user_answer : str, user_data) -> None:
        user_data.set(self.type, user_answer)
