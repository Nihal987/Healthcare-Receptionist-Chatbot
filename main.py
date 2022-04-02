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
from Google_nearby import get_nearby
from Appointments import create_appointment, show_appointments

def bot_speak(bot_text,audio=True):
    print("Bot text: ",bot_text)
    if audio:
        '''I'm using gTTS to generate Text-to-Speech.
        Uncomment the below lines to make it run without internet'''
        # engine = pyttsx3.init(driverName='nsss')
        # voices = engine.getProperty('voices')
        # engine.setProperty('voice', voices[0].id)
        # engine.say(bot_text)
        # engine.runAndWait()

        #Comment these lines and uncomment above lines to make it run without internet
        tts = gTTS(bot_text,lang='en')
        audio_file = 'voice.mp3'
        tts.save(audio_file)
        time.sleep(0.75)
        playsound.playsound(audio_file)
    

def user_input(mic=True):
    '''Function to obtain the user input either via
    the microphone or via the keyboard'''
    if mic:
        print("User text: ")
        voice_prompt = 'voice_prompt.mp3'
        playsound.playsound(voice_prompt)
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
            user_text = ""
        try:
            user_text = r.recognize_google(audio)
            print(user_text)
        except Exception as e:
            user_text = "Yes"
    else:
        user_text = input("Enter text: ")
    return user_text

def main():

    bot_text = "Something"
    user_text = "Hello"
    mic = True                                          # If the user is using voice inputs or not
    not_start = False

    while user_text!="end":
        
        # mic = False
        if not_start:                                       # First utterance of the bot is the welcome message
            user_text = user_input(mic)                        # Input from the user
            if user_text=="end":
                break
        
        response = get_response(user_text)
        response_text = response.query_result.fulfillment_text
        if len(response_text)>10 and (response_text[:9] == "Thank you" or response_text[:10]=="Sure thing"):    # Display appointment details
            """
            Here I am using the first two words of the response to detect the intent,
            I am not using response.query_result.intent.display_name as this intent has slots.
            Because it has slots the intent keeps looping until all the slots are filled. I use
            the first tow words of the response to tell when the loop is done, all the slots are filled.
            """ 
            bot_text,details = extract_details(response_text)
            bot_speak(bot_text)
            show_appointment_details(details)
            bot_speak('Here are your appointment details, is everything alright with you?')
            mic = True
        elif response.query_result.intent.display_name == 'appointment.book.slot':
            bot_speak(response_text)
            if "slot" in response_text:
                mic = False
            else:
                mic = True
        elif response.query_result.intent.display_name == 'appointment.book.details':   # Type in the user details (typing in as the STT software can't get non western names and emails)
            bot_speak(response_text)
            if "email" in response_text:
                mic = False
            else:
                mic = True
        elif response.query_result.intent.display_name == 'appointment.book.list':  # Display the list of doctors
            bot_speak(response_text)
            list_doctors(str(response.query_result))
            mic = True
        elif response.query_result.intent.display_name == 'appointment.confirm.yes':    # Confirm appointment details, create appointment
            create_appointment()
            send_email()
            bot_speak(response_text)
            mic = True
        elif response.query_result.intent.display_name == 'appointment.calendar.yes':   # Add appointment to Google Calendar
            create_event(details)
            bot_speak(response_text)
            mic = True
        elif response.query_result.intent.display_name == 'appointment.calendar.yes - no' or\
         response.query_result.intent.display_name == 'appointment.calendar.no - no':   # No more action required from chatbot
            user_text = "end"
            bot_speak(response_text)
            mic = True
        elif response.query_result.intent.display_name == 'nearby.type':    # Find close by pharmacies etc
            text = response_text.split("|")
            response_text = text[0]
            bot_speak(response_text)
            second_response = get_nearby(text[1].strip())
            bot_speak(second_response)
            user_text = "end"
        elif response.query_result.intent.display_name == 'appointment.show':   # Show all appointments
            bot_speak(response_text)
            show_appointments()
            user_text = "end"
        else:
            bot_speak(response_text)
            mic = True
        not_start = True
        
if __name__ == "__main__":
    main()