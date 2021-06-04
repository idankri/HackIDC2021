from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from conversation_manager import main_conversation_manager

app = Flask(__name__)

TWILIO_NUMBER = "+14155238886"
account_sid = 'AC6bb703567bab46b4b8c2dff452892fb5'
auth_token = '86add94c5884e3dcef8298494dca251b'


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
        from_='whatsapp:+14155238886',
        body=text,
        to=f'whatsapp:{number}'
    )
    print(message.sid)


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