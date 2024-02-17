from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

import requests


def report(config, logfile, empty_logfile=False):
    body = _read_content(logfile)
    fail = "fail" in body.lower()
    subject = "Borg backup FAILURE" if fail else "Borg backup success"

    _send_mail(config, subject, body)
    if fail:
        _send_telegram(config, subject)
    if empty_logfile:
        _empty_file(logfile)


def _send_mail(config, subject, body):
    conf = config["email"]
    email_from, email_to = conf["email"]["from"], conf["email"]["to"]
    smtp_host, smtp_port = conf["smtp"]["host"], conf["smtp"]["port"]
    username, password = conf["auth"]["username"], conf["auth"]["password"]

    msg = MIMEMultipart()
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = subject
    msg.attach(MIMEText(body))

    smtp = SMTP(smtp_host, smtp_port)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(email_from, email_to, msg.as_string())
    smtp.quit()


def _read_content(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line for line in lines if "permission denied" not in line.lower()]
    return "".join(lines)


def _send_telegram(config, subject):
    conf = config["telegram"]
    chat_id, token = conf["chat_id"], conf["token"]
    payload = {"chat_id": chat_id, "text": subject}
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=payload,
    )


def _empty_file(filename):
    open(filename, "w").close()
