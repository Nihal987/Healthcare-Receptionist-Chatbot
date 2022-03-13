import os
import os.path
import time
import datetime
from urllib import response
# import pyttsx3
import speech_recognition as sr
import pytz
from dialogflow import get_response
from utils import extract_details
from display_data import show_appointment_details, list_doctors
from Handle_calendar import create_event
from email_test import send_email

def bot_speak(bot_text):
    print("Bot text: ",bot_text)

def main():

    bot_text = "Something"
    user_text = "Something"
    while user_text!="end":
        user_text = input("User: ") # Input from the user
        if user_text=="end":
            break
        response = get_response(user_text)
        temp_text = response.query_result.fulfillment_text
        if len(temp_text)>10 and (temp_text[:9] == "Thank you" or temp_text[:10]=="Sure thing"):
            """
            Here I am using the first two words of the response to detect the intent,
            I am not using response.query_result.intent.display_name as this intent has slots.
            Because it has slots the intent keeps looping until all the slots are filled. I use
            the first tow words of the response to tell when the loop is done, all the slots are filled.
            """ 
            bot_text,details = extract_details(response.query_result.fulfillment_text)
            print("************")
            print(details)
            print("************")
            bot_speak(bot_text)
            show_appointment_details(details)
        elif response.query_result.intent.display_name == 'appointment.book.list':
            bot_speak(response.query_result.fulfillment_text)
            list_doctors(str(response.query_result))
        elif response.query_result.intent.display_name == 'appointment.confirm.yes':
            send_email()
            bot_speak(response.query_result.fulfillment_text)
        elif response.query_result.intent.display_name == 'appointment.calendar.yes':
            create_event(details)
            bot_speak(response.query_result.fulfillment_text)
        else:
            bot_speak(response.query_result.fulfillment_text)

if __name__ == "__main__":
    main()