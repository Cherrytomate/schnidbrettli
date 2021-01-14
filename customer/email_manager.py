# The first step is always the same: import all necessary components:
import smtplib
from socket import gaierror
import os

def review_handler(to_adress,surname):
    first_name = str(surname)
    port = 587
    smtp_server = os.getenv("SMTP_SERVER")
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    # Specify the senderâ€™s and receiverâ€™s email addresses:
    sender = "?????"
    receiver = "?????"

    # Type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
    message = f"""From: info@wettbewerb <info@wettbewerb-info.ch>
To: Jeremy <{to_adress}>
                
Content-type: text/html
Subject: Review

Hallo {first_name}, bitte fuelle doch noch eine Rezession aus!

<html>
  <body>
    <div id='body'>
      <p>Hi Pierce,</p>
      <p class='colored'>This text is blue.</p>
      <p>Jerry</p>
    </div>
  </body>
</html>
"""
    try:
        # Send your message with credentials specified above
        with smtplib.SMTP(smtp_server, port) as server:
            server.login(login, password)
            server.sendmail(sender, receiver, message)
    except (gaierror, ConnectionRefusedError):
        # tell the script to report if your message was sent or which errors need to be fixed
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Sent')