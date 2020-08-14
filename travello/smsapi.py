from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC0558096b3ceb11e2eef1c0f205e7c540'
auth_token = 'c43ce38ce0920dfbbd94e0ea82aa1744'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+12029535944',
         to='+918329258755'
     )

print(message.sid)