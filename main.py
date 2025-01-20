from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# Define Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    """Authenticate the user and return the Gmail API service."""
    creds = None
    # Check for existing token.pickle (stored credentials)
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Authenticate if no valid credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def search_emails(service, query):
    """Search Gmail inbox using a query and return matching messages."""
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    return messages

def count_job_applications():
    """Count the number of job applications based on keywords."""
    service = authenticate_gmail()

    # Keywords to search for in Gmail
    keywords = [
        'Thank you for applying',
        'Your application was sent',
        'We received your application',
        'Application submitted successfully'
    ]

    total_applications = 0

    for keyword in keywords:
        messages = search_emails(service, keyword)
        total_applications += len(messages)

    print(f"You have applied to {total_applications} jobs so far.")

if __name__ == '__main__':
    count_job_applications()
