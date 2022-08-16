# Simple Mail Transfer Protocol
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddres = "brunacrespomello@gmail.com"
toaddres = "brunacrespomello@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddres
msg['To'] = toaddres

msg['Subject'] = 'Python Mail Test'

body = """Test message from Python Mail Test"""

msg.attach(MIMEText(body, 'plain'))

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddres, '')

text = msg.as_string()

s.sendmail(fromaddres, toaddres, text)

s.quit()







