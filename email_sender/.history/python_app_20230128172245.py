from email import EmailMessage
import ssl
import smtplib


email_sender = 'venu2699@gmail.com'
email_password = 'xwwxzlkukekgqfwi'

email_receiver = 'zoltilurtu@gufum.com'

subject = "hi this is you!!"
body = """
Keep going!! dont stop hustling!
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

