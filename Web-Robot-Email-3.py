# Simple Mail Transfer Protocol
import smtplib
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

html = """
<html>
<body>
    <p>Title</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
        dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

<a href="https://github.com/BrunaMello/python-bot/commits?author=BrunaMello">Clique Aqui!!!!</a>
</body>
</html>"""

part1 = MIMEText(html, "html")

msg.attach(part1)


# SMTP server configuration
s = smtplib.SMTP('smtp.gmail.com', 587)

# Starting TTLS protocol
s.starttls()

# Login email
s.login(fromaddres, 'password')

# Change everything as a string
text = msg.as_string()

# Sending email
s.sendmail(fromaddres, toaddres, text)


# Close server
s.quit()







