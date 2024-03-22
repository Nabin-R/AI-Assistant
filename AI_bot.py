from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# if cloning from github use pip install on: speedrecognition, pyttsx3, wikipedia and wolframalpha.

# Initial Prompt for the AI - Change how you see fit.
INITIAL_PROMT = [
"You are a streamer's AI assistant",
"Your name is ONYX",
"Give a quick response, 1 sentence max.",
"Do Not Repeat questions",
"Do Not start the reply with your own name."
"Reply as if you are talking to the person the message is intended for."
"Here is a question:"
]
