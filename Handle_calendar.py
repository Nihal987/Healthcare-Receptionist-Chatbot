from __future__ import print_function

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import os
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    # Authenticate the Googgle credentials

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
    except HttpError as error:
        print('An error occurred: %s' % error)

    return service

def get_events(num):
    # Authenticate the Google credentials
    service = authenticate_google()

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=num,singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return

    # Prints the start and name of the next 10 events
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def create_event(details):
    service = authenticate_google()

    # Extracting time data
    date = details['date'].split('T')[0]
    ti = details['time']

    # temp = details['time']
    # temp = temp.split('T')
    # date = temp[0]
    # ti=  temp[1]
    # ti = ti.split('-')[0]
    dt = date+" "+ti.strip()
    d = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

    # Formatting the event details
    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    # Appointment details
    summary = "Appointment Booked " + details['appointment']
    doctor = details['doctor']
    description = "Appointment with Dr "+ doctor

    # Creating an appointment
    event_result = service.events().insert(calendarId='primary',
        body={
            "summary": summary,
            "description": description,
            "start": {"dateTime": start, "timeZone": 'America/Toronto'},
            "end": {"dateTime": end, "timeZone": 'America/Toronto'},
        }
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])
    print("\n")
