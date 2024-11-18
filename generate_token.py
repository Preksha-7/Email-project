from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

# Scopes for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_user():
    creds = None
    token_path = 'token.pickle'

    # Load existing token if available
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    # Generate a new token if none exists or expired
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)  # Use local server for desktop apps

        # Save the new token for future use
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

authenticate_user()
