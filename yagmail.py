import yagmail

def send_yag(to_email, subject, contents):
    yag = yagmail.SMTP()
    yag.send(to_email, subject, contents)
