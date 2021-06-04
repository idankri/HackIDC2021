from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import TwilioRestClient
from conversation_manager import main_conversation_manager

app = Flask(__name__)

ACCOUNT_SID = "AC6bb703567bab46b4b8c2dff452892fb5"
AUTH_TOKEN = "5db8253e5a4f855a90051e4874479661"
TWILIO_NUMBER = "+14155238886"


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
        msg.body(response_message)
    return str(resp)

def sendMessage(text, number):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        number,
        TWILIO_NUMBER,
        text)

'''
@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)
'''

if __name__ == '__main__':
    app.run()