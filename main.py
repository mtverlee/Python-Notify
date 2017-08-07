#pythonNotify
#By: Matt VerLee
#mtverlee@mavs.coloradomesa.edu
#https://github.com/mtverlee/

#MIT License

#Copyright (c) 2017 Matt VerLee

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import requests
import json
import httplib
import urllib
import smtplib
from time import strftime
import better_exceptions
better_exceptions.MAX_LENGTH = None


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
            "text": str(message)
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    print(r.status_code, r.reason)

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

def sendDiscordWebook(url, message, avatar_url):
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "content": str(message)
        "avatar_url": str(avatar_url)
    })
    r = requests.post(url, headers=headers, data=data)
    print(r.status_code, r.reason)