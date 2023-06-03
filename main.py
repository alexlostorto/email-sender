from src.email import Email


def main():
    email = Email()
    text = None
    html = None

    for i in range(len(email.to)):
        # Automatically change the name in the email
        if len(email.to[i]) > 1:
            text = email.text.replace('[Name]', email.to[i][1])
            html = email.html.replace('[Name]', email.to[i][1])
        email.createMessage(text, html)
        email.message['To'] = email.to[i][0]
        email.send()


if __name__ == '__main__':
    main()
