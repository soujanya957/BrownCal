from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_event(data):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': data['summary'],
        'location': data['location'],
        'description': data['description'],
        'start': {
            'dateTime': data['start_time'].isoformat(),
            'timeZone': 'Your timezone',
        },
        'end': {
            'dateTime': data['end_time'].isoformat(),
            'timeZone': 'Your timezone',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
