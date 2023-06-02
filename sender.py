from src.email import Email


def main():
    email = Email()
    for recipient, name in email.to:
        text = email.text.replace('[Company Name]', name)
        html = email.html.replace('[Company Name]', name)
        email.createMessage(text, html)
        email.message['To'] = recipient
        email.send()


if __name__ == '__main__':
    main()