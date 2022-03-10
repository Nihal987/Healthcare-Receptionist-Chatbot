from utils import extract_type, DATABASE

def show_appointment_details(details):
    
    # Extracting the Date data
    MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December']
    date = details['date'].split('T')[0]
    date = date.split('-')
    year = date[0]
    month = MONTHS[int(date[1])-1]
    day = date[2]

    # Extracting the time data
    time = details['time']
    time = time.split('T')[1]
    time = time.split('-')[0]
    
    # Printing the details of the appointment
    print("\nAPPOINTMENT DETAILS")
    print(f"PATIENT NAME: {details['name']}")
    print(f"EMAIL ADDRESS: {details['email']}")
    print(f"SPECIALIST TYPE: {details['appointment']}")
    print(f"DOCTOR: {details['doctor']}")
    print(f"DATE: {day} {month} {year}")
    print(f"TIME: {time[:-3]}\n")

def list_doctors(sentence):
    type = extract_type(sentence)
    print("\n")
    print(DATABASE[DATABASE['Specialization'] == type].head())
    print("\n")