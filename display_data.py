from utils import extract_type, DATABASE

def get_date(date_text):
    # Extracting the Date data
    MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December']
    date = date_text.split('T')[0]
    date = date.split('-')
    date = date[2] + " " + MONTHS[int(date[1])-1] + " " + date[0]
    # year = date[0]
    # month = MONTHS[int(date[1])-1]
    # day = date[2]
    return date

def get_time(time_text):
    # Extracting the time data
    time = time_text
    time = time.split('T')[1]
    time = time.split('-')[0]
    return time[:-3]

def show_appointment_details(details):
    
    # Printing the details of the appointment
    print("\nAPPOINTMENT DETAILS")
    print(f"PATIENT NAME: {details['name']}")
    print(f"EMAIL ADDRESS: {details['email']}")
    print(f"SPECIALIST TYPE: {details['appointment']}")
    print(f"DOCTOR: {details['doctor']}")
    print(f"DATE: {get_date(details['date'])}")
    print(f"TIME: {get_time(details['time'])}\n")

def list_doctors(sentence):
    type = extract_type(sentence)
    print("\n")
    print(DATABASE[DATABASE['Specialization'] == type].head())
    print("\n")