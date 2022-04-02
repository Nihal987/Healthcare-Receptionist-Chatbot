import pandas as pd
from utils import DETAILS
from display_data import get_date

def create_appointment():
    doc_info = pd.read_excel('Doctor_database.xlsx')
    # Getting the Branch information
    branch = doc_info[(doc_info['Name'] == DETAILS['doctor']) & (doc_info['Specialization']==DETAILS['appointment'])]['Branch'].item() 
    appointment = pd.read_excel('Appointment_database.xlsx')
    app = {'Patient Name': DETAILS['name'],
        'Doctor Name': DETAILS['doctor'],
        'Specialist Type': DETAILS['appointment'],
        'Branch': branch,
        'Date':get_date(DETAILS['date']),
        'Time':DETAILS['time']}
    appointment = appointment.append(app,ignore_index=True)   
    appointment.to_excel('Appointment_database.xlsx',index=False)