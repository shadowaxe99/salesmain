
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_address, subject, message, from_address="salesman.ai.agent@gmail.com", password="password"):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

def generate_email(lead_name, company_name):
    subject = f"Business Proposal for {company_name}"
    message = f"Dear {lead_name},\n\nWe have a business proposal for {company_name}.\n\nBest,\nSalesman AI Agent"
    return subject, message
