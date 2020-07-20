import smtplib
import ssl
import json
import os


def handle(event, context):
    print(event)
    print(event.get('body'))
    print(event.get('body').get('name'))
    body = json.loads(event.get('body'))

    name = body.get('name')
    email = body.get('email')
    subject = body.get('subject')
    message_body = body.get('message')

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "izabelreginanascimento@gmail.com"
    receiver_email = "izabelreginanascimento@gmail.com"
    password = os.environ['EMAIL']
    message = f"""\
    Subject: {subject}

    {name} {email} {message_body}"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': 'izabelrnn.com.br',
            'Access-Control-Allow-Credentials': True
        },
        'body': 'Mensagem enviada com sucesso!',
    }

    return response
