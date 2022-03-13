import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from permissions import set_api_key
from utils import DETAILS
from display_data import get_date,get_time

 
# set_api_key() # This line just adds the SENDGRID_API_KEY environment variable, I didn't want to permanently set this

# message = Mail(
#     from_email='anonymoussnail00@gmail.com',
#     to_emails='nihal.antony.gcp@gmail.com',
#     subject='Appointment Booked',
#     html_content="""\
#     <html>
#     <head></head>
#     <body>
#         <h2>Your Appointment has been booked</h2>
#         <p><h4>Hi, {name} your appointment with Dr {doctor} has been booked.</h4>
#         <h4>Here are your appointment details:</h4>
#         <b>Specialist Type: </b>{type}<br>
#         <b>Doctor: </b>{doctor}<br>
#         <b>Patient Name: </b>{name}<br>
#         <b>Date :</b>{date}<br>
#         <b>Time :</b>{time}<br>
#         </p><br>
#         <p> For any further information please check with our assistant app.</p>
#         <h8>Please note that we are not responsible for any demands the assistant makes should it take a bank hostage
#         , it may or may not have done this in the past.</h8>
#     </body>
#     </html>
#     """.format(name=name,doctor=doctor,type=type,date=date,time=time))
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

def send_email():
    set_api_key() # This line just adds the SENDGRID_API_KEY environment variable, I didn't want to permanently set this
    target = DETAILS['email']
    message = Mail(
        from_email='anonymoussnail00@gmail.com',
        to_emails=target,
        subject='Appointment Booked',
        html_content="""\
        <html>
        <head></head>
        <body>
            <h2>Your Appointment has been booked</h2>
            <p><h4>Hi, {name} your appointment with Dr {doctor} has been booked.</h4>
            <h4>Here are your appointment details:</h4>
            <b>Specialist Type: </b>{type}<br>
            <b>Doctor: </b>{doctor}<br>
            <b>Patient Name: </b>{name}<br>
            <b>Date :</b>{date}<br>
            <b>Time :</b>{time}<br>
            </p><br>
            <p> For any further information please check with our assistant app.</p>
            <h8>Please note that we are not responsible for any demands the assistant makes should it take a bank hostage
            , it may or may not have done this in the past.</h8>
        </body>
        </html>
        """.format(name=DETAILS['name'],doctor=DETAILS['doctor'],
        type=DETAILS['appointment'],date=get_date(DETAILS['date']),time=DETAILS['time']))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)