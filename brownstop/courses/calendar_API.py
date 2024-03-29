from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime

CAL_ID = "2d4b40ced10733cff49427eb93b6ef8086e87ce3dcf52e13bbcca385b0446f77@group.calendar.google.com"
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './google-credentials.json'


def test_calendar(summary, location, description, syear, smonth, sday, eyear, emonth, eday, timezone):
    print("RUNNING TEST_CALENDAR()")

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # CREATE A NEW EVENT
    new_event = {
    'summary': summary,
    'location': location,
    'description': description,
    'start': {
        'date': f"{datetime.date(int(syear), int(smonth), int(sday))}",
        'timeZone': timezone,
    },
    'end': {
        'date': f"{datetime.date(int(eyear), int(emonth), int(eday))}",
        'timeZone': timezone,
    },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

 # GET ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])

    # LOG THEM ALL OUT IN DEV TOOLS CONSOLE
    for e in events:
        print(e)

    #uncomment the following lines to delete each existing item in the calendar
    #event_id = e['id']
        # service.events().delete(calendarId=CAL_ID, eventId=event_id).execute()


    return events
