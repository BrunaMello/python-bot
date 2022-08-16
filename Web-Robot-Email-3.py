# Simple Mail Transfer Protocol
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email sender
fromaddres = "brunacrespomello@gmail.com"

# Email receiver
toaddres = "brunacrespomello@gmail.com"

# Editing parts from email
msg = MIMEMultipart()

# From
msg['From'] = fromaddres

# To
msg['To'] = toaddres

# Subject
msg['Subject'] = 'Python Mail Test'

# Body
body = """Test message from Python Mail Test"""

# Editing
msg.attach(MIMEText(body, 'plain'))

# Attachment
filename = 'result.txt'

attach = open('result.txt', 'rb')

# Saving attach inside computer memory
p = MIMEBase('application', 'octet-stream')

p.set_payload(attach.read())

# Coding to 64-bit
encoders.encode_base64(p)

# Reader
p.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)

msg.attach(p)


# SMTP server configuration
s = smtplib.SMTP('smtp.gmail.com', 587)

# Starting TTLS protocol
s.starttls()

# Login email
s.login(fromaddres, '')

# Change everything as a string
text = msg.as_string()

# Sending email
s.sendmail(fromaddres, toaddres, text)


# Close server
s.quit()







