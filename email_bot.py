import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener=sr.Recognizer()
engine=pyttsx3.init()

email_list={
    "mom":"shrabanimanna22@gmail.com",
    "dad":"smanna2404@gmail.com",
    "arushi":"guptaarushi.06@gmail.com",
    "myself":"smanna1504@gmail.com"
}

def talk(text):
    
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('smanna1504@gmail.com','smanna@123')

    email=EmailMessage()
    email["From"]="smanna1504@gmail.com"
    email["To"]=receiver
    email["Subject"]=subject
    email.set_content(message)
    server.send_message(email)
    print("Voila! Your email is successfully sent!!!!")

def get_email_info():
    talk('To whom you want to send email?')
    name=get_info()
    receiver=email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject=get_info()
    talk('Tell me the body of the email')
    message=get_info()
    send_email(receiver,subject,message)

get_email_info()
