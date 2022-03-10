import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from permissions import set_api_key
 
set_api_key() # This line just adds the SENDGRID_API_KEY environment variable, I didn't want to permanently set this
message = Mail(
    from_email='anonymoussnail00@gmail.com',
    to_emails='nihal.antony.gcp@gmail.com',
    subject='Appointment Booked',
    html_content='<strong>Appointment has been booked/strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)