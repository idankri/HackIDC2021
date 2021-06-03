from question_pool import QuestionPool


class PhoneNotExistsError(Exception):
    pass


class InvalidMessageError(Exception):
    pass


main_question_pool = QuestionPool()
