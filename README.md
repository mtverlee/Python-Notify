# pythonNotify
Simple Python notification library.
Currently supports:
- Facebook Messages
- Pushover Notifications
- Gmail
- Discord Webhooks

## Use:
```
git submodule add -f https://gitub.com/mtverlee/pythonNotify.git notifications
import notifications.main as notifications
```
To send a FB Message:
```
notifications.sendFBMessage(token, recipient, message)
```
To send a Pushover notification:
```
notifications.sendPushoverNotification(appToken, userToken, message, title, priority)
```
To send an email:
```
notifications.sendEmail(recipient, subject, text, emailUsername, emailPassword)
```
To send a Discord webhook:
```
notifications.sendDiscordWebhook(url, username, avatar_url, content)
```