from twilio.rest import Client

client = Client("", "")


def sendmessage(body, to):
    message = client.messages \
        .create(
        body=body,
        from_='+14793481569',
        to=to
    )

    print(message.sid)
