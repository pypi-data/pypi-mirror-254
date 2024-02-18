# mailblaster/mailblaster.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def read_credentials(filename):
    credentials = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                credentials.append((parts[0], parts[1], parts[2], int(parts[3])))
    return credentials

def read_recipients(filename):
    recipients = []
    with open(filename, 'r') as file:
        for line in file:
            recipients.append(line.strip())
    return recipients

def read_html_content(filename):
    with open(filename, 'r') as file:
        html_content = file.read()
    return html_content

def remove_email_from_file(filename, email):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if line.strip() != email:
                file.write(line)

def send_emails(sender_email, sender_password, smtp_server, smtp_port, recipient_email, html_content):
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Stellenanzeigen schalten - AngebotVerteiler.com"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Create the body of the message (HTML version)
    part2 = MIMEText(html_content, 'html')

    # Attach HTML part to the message
    msg.attach(part2)

    # Send the message via SMTP server
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [recipient_email], msg.as_string())
        print(f"Email sent successfully from {sender_email} to {recipient_email}")

        # Remove the sent email from the recipient list file
        remove_email_from_file("recipient.txt", recipient_email)
        
        # Append sent email address to sent.txt
        with open('sent.txt', 'a') as sent_file:
            sent_file.write(recipient_email + '\n')

    except Exception as e:
        print(f"Unable to send email from {sender_email} to {recipient_email}:", e)

# Read sender credentials and recipient emails
sender_credentials = read_credentials("sender.txt")
recipient_emails = read_recipients("recipient.txt")
html_content = read_html_content("email_template.html")

# Iterate over recipient emails
for i, recipient_email in enumerate(recipient_emails):
    # Select sender credentials based on index
    sender_email, password, smtp_server, smtp_port = sender_credentials[i % len(sender_credentials)]
    
    # Send email
    send_emails(sender_email, password, smtp_server, smtp_port, recipient_email, html_content)
    
    # Add a delay between each email (adjust as needed)
    time.sleep(5)  # 5 seconds delay
