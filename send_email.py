import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pickle

def send_email_via_gmail(subject, body, to_email, from_email):
    # Load credentials from token.pickle
    creds = None
    try:
        with open('token.pickle', 'rb') as token_file:
            creds = pickle.load(token_file)
    except FileNotFoundError:
        raise Exception("Token file not found. Please authenticate again.")

    # Refresh the token if expired
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=creds)

    # Create the email message
    message = MIMEText(body)
    message['to'] = to_email
    message['from'] = from_email
    message['subject'] = subject

    # Encode the message
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send the email
    message_body = {'raw': raw_message}
    try:
        service.users().messages().send(userId='me', body=message_body).execute()
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        raise Exception(f"Failed to send email: {str(e)}")
