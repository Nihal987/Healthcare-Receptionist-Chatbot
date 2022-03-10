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

def bot_speak(bot_text):
    print("Bot text: ",bot_text)

def main():

    bot_text = "Something"
    user_text = "Something"
    while user_text!="end":
        user_text = input("User: ")
        if user_text=="end":
            break
        response = get_response(user_text)
        temp_text = response.query_result.fulfillment_text
        if len(temp_text)>10 and temp_text[:9] == "Thank you":
            bot_text,details = extract_details(response.query_result.fulfillment_text)
            bot_speak(bot_text)
            show_appointment_details(details)
        elif response.query_result.intent.display_name == 'appointment.book.list':
            bot_speak(response.query_result.fulfillment_text)
            list_doctors(str(response.query_result))
            
        else:
            bot_speak(response.query_result.fulfillment_text)

if __name__ == "__main__":
    main()