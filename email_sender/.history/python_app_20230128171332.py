from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'venu2699@gmail.com'
email_password = 'xwwxzlkukekgqfwi'

email_receiver = ''

subject = "hi this is you!!"
body = """
Keep going!! dont stop hustling!
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

