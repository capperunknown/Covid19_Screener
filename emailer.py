import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

email = "abdul.hafeezm02@gmail.com" 
password = ""
#send_to_email = "k.burrell@mistersafetyshoes.com"
send_to_email = "capper.unknown@protonmail.com"

today = date.today()
dates = today.strftime("%B %d, %Y")

subject = 'COVID-19 worker and employee screening | passed | {}'.format(dates)
message = """{}

COVID-19 worker and employee screening result: passed

=====================

This result is no longer valid if your situation changes during the day (for example, you start experiencing symptoms).

https://covid-19.ontario.ca/screening/worker/

====================

This email is your personal record to archive or share. Please do not alter, modify or delete any of the content.
The Government of Ontario does not record or retain your responses to our COVID-19 self-assessments, and we are not able to confirm the accuracy or authenticity of individual results.
""".format(dates)

print('Preparing to send email...')
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = send_to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()

    server.sendmail(email, send_to_email, text)
    server.quit()

except Exception as e: print(e)

else:
    print('Email(s) Sent Successfully')