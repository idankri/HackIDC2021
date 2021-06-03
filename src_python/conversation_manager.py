from globals import *
from utils.singleton import Singleton
from conversation import Conversation
from collections import defaultdict


class ConversationManager(metaclass=Singleton):
    def __init__(self):
        self.id_to_conversation = defaultdict(Conversation)

    def get_conversation(self, conversation_id: str):
        if conversation_id in self.id_to_conversation:
            return self.id_to_conversation[conversation_id]
        else:
            raise PhoneNotExistsError("Phone not found")

    def process_message(self, conversation_id, message):
        return self.id_to_conversation[conversation_id].process_message(message)

    def process_image(self, conversation_id, image_data):
        return self.id_to_conversation[conversation_id].process_image(image_data)


