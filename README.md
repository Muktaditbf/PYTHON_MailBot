# 📧 Python MailBot

A minimal Python script that sends an email through Gmail using the built-in `smtplib` library. No extra packages needed.

## How it works

1. Connects to Gmail's SMTP server on port 587
2. Switches to an encrypted connection with `starttls()`
3. Logs in and sends a plain-text message

## Setup

1. Turn on **2-Step Verification** on your Google account.
2. Create an **App Password** at <https://myaccount.google.com/apppasswords>. Your normal Gmail password won't work.
3. In `py-mail-bot.py`, fill in `my_email`, `my_password` (the app password) and `receiver_mail`.

## Run it

```bash
python py-mail-bot.py
```

> ⚠️ Never commit your real email or app password to GitHub. A safer version would read them from environment variables, for example `os.environ["MAIL_PASSWORD"]`.

## Ideas for improvement

- Load credentials from environment variables or a `.env` file
- Use `email.message.EmailMessage` for proper subjects, HTML and attachments
- Send to a list of recipients
