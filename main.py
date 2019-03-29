import os
import requests
import json
import http.client
import urllib
import smtplib
from time import strftime
import sentry_sdk
sentry_sdk.init("https://4faf1b442d25479a87f6789bea08eb9d@sentry.io/1420507")

def sendFBMessage(token, recipient, message):
    try:
        params = {
            "access_token": token
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient
            },
            "message": {
                "text": str(message)
            }
        })
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
        print(r.status_code, r.reason)
    except Exception as e:
        sentry_sdk.capture_exception(e)

def sendPushoverNotification(appToken, userToken, message, title, priority):
    try:
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": appToken,
            "user": userToken,
            "message": message,
            "title": title,
            "priority": priority,
            "retry": 300,
            "expire": 3600,
        }), { "Content-type": "application/x-www-form-urlencoded" })
        print(conn.getresponse())
    except Exception as e:
        sentry_sdk.capture_exception(e)

def sendEmail(recipient, subject, text, emailUsername, emailPassword):
    try:
        TIME = strftime("%H:%M:%S")
        TO = recipient
        SUBJECT = subject
        TEXT = text
        # Gmail Sign In
        gmail_sender = emailUsername
        gmail_passwd = emailPassword
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        try:
            server.sendmail(gmail_sender, [TO], BODY)
            pass
        except Exception as e:
            print('Encountered exception - ' + e + '.')
            pass
        server.quit()
    except Exception as e:
        sentry_sdk.capture_exception(e)

def sendDiscordWebhook(url, username, avatar_url, content):
    try:
        headers = {
            "Content-Type" : "application/json"
        }
        data = {
            "username": str(username),
            "avatar_url": str(avatar_url),
            "content": str(content)
        }
        r = requests.post(str(url), json=data, headers=headers)
    except Exception as e:
        sentry_sdk.capture_exception(e)
