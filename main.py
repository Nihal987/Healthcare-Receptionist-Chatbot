import os
import os.path
import time
import datetime
from urllib import response
# import pyttsx3
import speech_recognition as sr
import pytz
from dialogflow import get_response

def main():

    bot_text = "Something"
    user_text = "Something"
    while bot_text!="end":
        user_text = input("User: ")
        if user_text=="end":
            break
        response = get_response(user_text)
        # if response.query_result.intent.display_name == "schedule appointment":
        #     book_appointment()
        bot_text = response.query_result.fulfillment_text
        print("Bot text: ",bot_text)

if __name__ == "__main__":
    main()