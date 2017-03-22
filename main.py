""" 

Python Facebook Notifier
Matt VerLee
mtverlee@mavs.coloradomesa.edu
https://github.com/mtverlee/

"""

""" Import required libraries. """
import os
import requests
import json
import httplib
import urllib
import smtplib
from time import strftime
import better_exceptions
better_exceptions.MAX_LENGTH = None


""" Functions. """
def sendFBMessage(token, recipient, message):
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
            "text": message
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    print(r.status_code)

def sendPushoverNotification(appToken, userToken, message, title):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
        "token": appToken,
        "user": userToken,
        "message": message,
        "title": title,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    print(conn.getresponse())

def sendEmail(recipient, subject, text, emailUsername, emailPassword):
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
