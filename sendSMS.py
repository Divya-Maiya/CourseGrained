from twilio.rest import Client

client = Client("AC1177934118fec786faba0612d95ed05f", "82166370513078fd73e2302b18ab39a3")


def sendmessage(body, to):
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+14793481569',
        to='+14132109736'
    )

    print(message.sid)
