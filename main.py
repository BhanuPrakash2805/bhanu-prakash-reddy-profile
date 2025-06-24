# app.py
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv() # Destination email
app = Flask(__name__)
# Configure your email credentials from environment variables
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
EMAIL_ADDRESS = os.getenv('livingkik1998@gmail.com')
EMAIL_PASSWORD = os.getenv('xica mrbh gice ozuh')  # Use App Password if 2FA enabled
RECEIVER_EMAIL = os.getenv('sbhanu281436@gmail.com')  # Destination email
CONTACT_EMAIL = os.getenv('sbhanu281436@gmail.com')  # Contact email for the form


@app.route('/send-message', methods=['POST'])
def send_message():
       # Check if server configuration is available
    if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, RECEIVER_EMAIL]):
        app.logger.error("Server email configuration is missing. Check .env file.")
        return jsonify({'error': 'Server configuration error.'}), 500
    data = request.json
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not all([name, email, subject, message]):
                return jsonify({'error': 'All fields (name, email, subject, message) are required.'}), 400


    body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}"

    msg = MIMEText(body)
    msg['Subject'] = f"New Contact Form Message: {subject}"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL
    msg['Reply-To'] = email # Allows direct reply to the user
    msg['X-Contact-Email'] = CONTACT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg.as_string())
        return jsonify({'message': 'Email sent successfully'})
    
    except smtplib.SMTPException as e:
        app.logger.error(f"Failed to send email: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)