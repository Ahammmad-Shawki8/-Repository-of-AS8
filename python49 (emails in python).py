# first we need to connect to the mail server.
# for that we need to import smtplib module.
import smtplib

# we will use context manager and SMTP() class.
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    # smtp.gmail.com is the gmail host and 587 is the port
    smtp.ehlo() 
    # ehlo() method identifies ourselves with the mailserver we are using.
    # now we need to encrypt our traffic with starttls() method.
    smtp.starttls()
    # now we need to rerun the ehlo() method again to reidenty ourself as an encrypted connection.
    smtp.ehlo()

    # now we will login to our mail server
    smtp.login("ahammadshawki8@gmail.com", "sample_password")
    # here we need to put in our email address and password.

    # now lets define the email properties.
    subject = "Testing Python Email Options"
    body = """
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """
    msg = f"Subject: {subject}\n\n{body}"

    # now we need to send the simple text email.
    smtp.sendmail("ahammadshawki8@gmail.com", "ahammadshawki8@outlook.com", msg)
    # from, to, msg

# we can send a simple email like this.
# sometimes we don't want to send too many emails to ourself.
# for that, we can create a debugging server which will listen to the emails and print on the cli.
# we have to execute this command-
"""python -m smtpd -c DebuggingServer -n localhost:1025"""
with smtplib.SMTP("localhost", 1025) as smtp:
    subject = "Testing Python Email Options"
    body = """
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """
    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail("ahammadshawki8@gmail.com", "ahammadshawki8@outlook.com", msg)


# Now lets send complex messages
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    # now we will use SMTP_SSL connection, we don't need those extra lines.

    smtp.login("ahammadshawki8@gmail.com", "sample_password")


    subject = "Testing Python Email Options"
    body = """
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """
    msg = f"Subject: {subject}\n\n{body}"
    # here is the formatting is weired.
    # to change the formatting we have to import EmailMessage class.

    smtp.sendmail("ahammadshawki8@gmail.com", "ahammadshawki8@outlook.com", msg)



# Change formatting
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "ahammadshawki8@gmail.com"
msg["To"] = "ahammadshawki8@outlook.com"
msg["Subject"] = "Testing Python Email Options"
msg.set_content("""
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("ahammadshawki8@gmail.com", "sample_password")
    # for sending mail we will use send_message method.
    smtp.send_message(msg)



# Sending attachments
from email.message import EmailMessage
import imghdr

msg = EmailMessage()
msg["From"] = "ahammadshawki8@gmail.com"
msg["To"] = "ahammadshawki8@outlook.com"
msg["Subject"] = "Testing Python Email Options"
msg.set_content("""
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """)

# open that file that we want to attach
with open("./pic/octocat.png", "rb") as pic:
    file_data = pic.read()
    # before sending images, we need to determine what kind of images we want to send.
    # imghdr method wil help us in that purpose.
    file_name = pic.name
    file_type = imghdr.what(file_name) # passing the name
    print(file_type)

# now lets attach our email,
msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("ahammadshawki8@gmail.com", "sample_password")
    smtp.send_message(msg)



# sending multiple images
from email.message import EmailMessage
import imghdr

msg = EmailMessage()
msg["From"] = "ahammadshawki8@gmail.com"
msg["To"] = "ahammadshawki8@outlook.com"
msg["Subject"] = "Testing Python Email Options"
msg.set_content("""
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """)

files = ["./pic/octocat.png", "./pic/winter.jpg", "./pic/winter_new.png"]

for file in files:
    with open(file, "rb") as pic:
        file_data = pic.read()
        file_name = pic.name
        file_type = imghdr.what(file_name)
        print(file_type)
    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("ahammadshawki8@gmail.com", "sample_password")
    smtp.send_message(msg)



# if we need to atach other kinds of files than we need change the maintype and subtype.
# sending pdf
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "ahammadshawki8@gmail.com"
msg["To"] = "ahammadshawki8@outlook.com"
msg["Subject"] = "Testing Python Email Options"
msg.set_content("""
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """)

files = ["./pic/cv.pdf"]

for file in files:
    with open(file, "rb") as pic:
        file_data = pic.read()
        file_name = pic.name
    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("ahammadshawki8@gmail.com", "sample_password")
    smtp.send_message(msg)


# sending email to multiple people
from email.message import EmailMessage

TO_LIST = ["ahammadshawki8@outlook.com", "blah-blah@outlook.com"]
msg = EmailMessage()
msg["From"] = "ahammadshawki8@gmail.com"
msg["To"] = ", ".join(TO_LIST)
msg["Subject"] = "Testing Python Email Options"
msg.set_content("""
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblahblahblahblahblahblahblahblahblahblahblahblahblah
        blahblahblahblah
        blahblahblahblahblahblahblahblah

        blahblahblahblahblahblah
        blahblah
        """)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("ahammadshawki8@gmail.com", "sample_password")
    smtp.send_message(msg)


# we may need to use html in oour email when we need newletters.
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "ahammadshawki8@gmail.com"
msg["To"] = "ahammadshawki8@outlook.com"
msg["Subject"] = "Testing Python Email Options"
msg.set_content("A plain text")

# adding html
msg.add_alternative("""
    <!Doctype html>
    <html lang="en">
        <body>
            <h1 style="color:greenyellow;">Hello World!</h1>
        </body>
    </html>
    """, subtype="html")


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("ahammadshawki8@gmail.com", "sample_password")
    smtp.send_message(msg)