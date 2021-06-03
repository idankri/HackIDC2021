from globals import *
from utils.singleton import Singleton
from conversation import Conversation


class ConversationManager(metaclass=Singleton):
    def __init__(self):
        self.id_to_conversation = dict()

    def get_conversation(self, conversation_id: str):
        if conversation_id in self.id_to_conversation:
            return self.id_to_conversation[conversation_id]
        else:
            raise PhoneNotExistsError("Phone not found")

    def process_message(self, conversation_id, message):
        if conversation_id in self.id_to_conversation:
            for message in self.id_to_conversation[conversation_id].process_message(message):
                yield message
        else:
            self.id_to_conversation[conversation_id] = Conversation(conversation_id)
            for message in self.id_to_conversation[conversation_id].process_message(message):
                yield message


    def process_image(self, conversation_id, image_data):
        if conversation_id in self.id_to_conversation:
            self.id_to_conversation[conversation_id].process_image(image_data)
        else:
            raise PhoneNotExistsError("Phone not found")


main_conversation_manager = ConversationManager()

if __name__ == '__main__':
    cm = ConversationManager()
    for message in cm.process_message("123456", "היי"):
        print(message)
    for message in cm.process_message("123456", "יניב"):
        print(message)
    a = 1


