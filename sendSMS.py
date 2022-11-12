from twilio.rest import Client

client = Client("AC1177934118fec786faba0612d95ed05f", "130527aa738694a3f32cccf6ede45b3f")


def sendmessage(body, to):
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+14793481569',
        to='+14132109736'
    )

    print(message.sid)
