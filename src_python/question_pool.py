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

# main_question_pool.add(Question(
#     type_of_item=None,
#     message_to_user="אהלן אהלן כאן משה הסוקר",
#     invalid_message=None,
#     answer_validation_function=None,
#     get_next_question_id=lambda user_msg: 2,
#     answer_flag=False,
#     image_flag=False
# ))

# main_question_pool.add(Question(
#     type_of_item=None,
#     message_to_user="אהלן אהלן כאן משה הסוקר" + "\n"
#                     "שמח שבחרת בביטוח ישיר 😃" + "\n"
#                     "אשמח לשאול אותך כמה שאלות ולתת לך הצעת ביטוח בקלות ובמהירות!",
#     invalid_message=None,
#     answer_validation_function=lambda x: True,
#     get_next_question_id=lambda user_msg: 1,
#     answer_flag=False,
#     image_flag=False
# ))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="Hello Moshe here!\nHow are you?",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 2,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="קודם כל עם מי יש לי את הכבוד לדבר?",
    invalid_message=None,
    answer_validation_function=lambda user_msg: not user_msg.isdigit(),
    get_next_question_id=lambda user_msg: 2,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="היי נעים להכיר!",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 4,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="אשמח לדעת מה הכתובת שלך",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 6,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="מה גודל הדירה במטר רבוע?",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 7,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="כמה חדרים בדירה?",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 8,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="מעולה! אני מסתכל על דירות דומות באזורך ואני רואה שערך תכולת הדירה הממוצע הוא בין 250 ל-300 אלף שקלים",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 9,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="לעשות ביטוח תכולת דירה זאת החלטה מעולה!",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 10,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="על מנת לתת לך הערכה יותר מדוייקת אשמח לשאול אותך כמה שאלות 😇",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 11,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="האם יש לך כמה דקות פנויות?",
    invalid_message="איזה באסה! תכתוב לי כן כשמתפנה",
    answer_validation_function=lambda x: "כן" in x,
    get_next_question_id=lambda user_msg: 12,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="מעולה!",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 13,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="נתחיל מהמטבח, רק אל תתפתה לעבור במקרר 😤",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 14,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="שווי תכולת מטבח ממוצע הינו 15 אלף שקלים. האם השווי נשמע לך הגיוני?",
    invalid_message=None,
    answer_validation_function=lambda x: "כן" in x or "לא" in x,
    get_next_question_id=lambda user_msg: 16 if "כן" in user_msg else 15,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="איזה באסה! אבל אני בוט מתחיל אז כרגע אני לא מבין במטבחים. ",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 16,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="https://cataas.com/cat",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 17,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="יופי! נעבור לסלון 🥳",
    invalid_message=None,
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 18,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="לדעתי יש לך בסלון ספה, שולחן, כורסא וטלוויזיה. האם שכחתי משהו?",
    invalid_message=None,
    answer_validation_function=lambda x: "כן" in x or "לא" in x,
    get_next_question_id=lambda user_msg: 19 if "לא" in user_msg else 22,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="אוי 🤯",
    invalid_message=None,
    answer_validation_function=lambda x: "כן" in x or "לא" in x,
    get_next_question_id=lambda user_msg: 20,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="אשמח אם תכוון אותי מה שכחתי",
    invalid_message=None,
    answer_validation_function=lambda x: x in ["תמונה"],
    get_next_question_id=lambda user_msg: 21,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="תמונה מוסיפה מלא לבית! מה המחיר של התמונה?י",
    invalid_message="סליחה אני לא מבין :(",
    answer_validation_function=lambda x: True,
    get_next_question_id=lambda user_msg: 22,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="מעולה! סך הכל שווי הסלון הינו 12000 שח. נשמע לך הגיוני?",
    invalid_message="איזה באסה, אבל אני בוט מתחיל אז אני אצטרך עזרה! תכף מוקדן שלנו יתקשר אליך",
    answer_validation_function=lambda x: "כן" in x,
    get_next_question_id=lambda user_msg: 23,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="מעולה! לפי החישובים שלי שווי תכולת הדירה הכולל שלך הוא 270 אלף שח ומחיר הביטוח הוא 872 שח לשנה",
    invalid_message="איזה באסה, אבל אני בוט מתחיל אז אני אצטרך עזרה! תכף מוקדן שלנו יתקשר אליך",
    answer_validation_function=lambda x: "כן" in x,
    get_next_question_id=lambda user_msg: 24,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="האם תרצה לשלם כעת?",
    invalid_message="איזה באסה, אבל אני בוט מתחיל אז אני אצטרך עזרה! תכף מוקדן שלנו יתקשר אליך",
    answer_validation_function=lambda x: "כן" in x,
    get_next_question_id=lambda user_msg: 25,
    answer_flag=True,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="מעולה! מיד נתקשר לבקש פרטי תשלום.",
    invalid_message="איזה באסה, אבל אני בוט מתחיל אז אני אצטרך עזרה! תכף מוקדן שלנו יתקשר אליך",
    answer_validation_function=lambda x: "כן" in x,
    get_next_question_id=lambda user_msg: 26,
    answer_flag=False,
    image_flag=False
))

main_question_pool.add(Question(
    type_of_item=None,
    message_to_user="שמחתי לעזור 🤩 שיהיה לך יום מדהים",
    invalid_message="איזה באסה, אבל אני בוט מתחיל אז אני אצטרך עזרה! תכף מוקדן שלנו יתקשר אליך",
    answer_validation_function=lambda x: "כן" in x,
    get_next_question_id=lambda user_msg: 26,
    answer_flag=False,
    image_flag=False
))