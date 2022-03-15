import os
import os.path
import time
import datetime
from urllib import response
# import playsound
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound
from dialogflow import get_response
from utils import extract_details
from display_data import show_appointment_details, list_doctors
from Handle_calendar import create_event
from email_test import send_email

def bot_speak(bot_text,audio=True):
    print("Bot text: ",bot_text)
    if audio:
        # engine = pyttsx3.init(driverName='nsss')
        # voices = engine.getProperty('voices')
        # engine.setProperty('voice', voices[0].id)
        # engine.say(bot_text)
        # engine.runAndWait()
        tts = gTTS(bot_text,lang='en')
        audio_file = 'voice.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)

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
            bot_speak(bot_text)
            show_appointment_details(details)
            bot_speak('Are the above details correct?')
        elif response.query_result.intent.display_name == 'appointment.book.list':
            bot_speak(response.query_result.fulfillment_text)
            list_doctors(str(response.query_result))
        elif response.query_result.intent.display_name == 'appointment.confirm.yes':
            send_email()
            bot_speak(response.query_result.fulfillment_text)
        elif response.query_result.intent.display_name == 'appointment.calendar.yes':
            create_event(details)
            bot_speak(response.query_result.fulfillment_text)
        elif response.query_result.intent.display_name == 'appointment.calendar.yes - no' or\
         response.query_result.intent.display_name == 'appointment.calendar.no - no':
            user_text = "end"
            bot_speak(response.query_result.fulfillment_text)
        else:
            bot_speak(response.query_result.fulfillment_text)

if __name__ == "__main__":
    main()