from twilio.rest import Client
import os

twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
client = Client(twilio_account_sid, twilio_auth_token)

message = client.messages \
                .create(
                     body="Hello, this is a text from Cris' app.",
                     from_='+12082258479',
                     to='+19739384730'
                 )

print(message.sid)