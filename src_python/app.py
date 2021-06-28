from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from conversation_manager import main_conversation_manager

app = Flask(__name__)

TWILIO_NUMBER = "" # Should be Twilio number
account_sid = '' # Should be Twilio account SID
auth_token = '' # Should be Twilio Auth token


@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    phone_number = request.values.get('From').split(':')[1]
    response_messages = main_conversation_manager.process_message(phone_number, incoming_msg)

    first = True
    for response_message in response_messages:
        if response_message is None or "https" in response_message:
            continue
        sendMessage(response_message, phone_number)
    return str(resp)

def sendMessage(text, number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=f'whatsapp:{TWILIO_NUMBER}',
        body=text,
        to=f'whatsapp:{number}'
    )
    print(message.sid)


if __name__ == '__main__':
    app.run()