import pyttsx3
import PyPDF2
import speech_recognition as sr

engine=pyttsx3.init()
listener=sr.Recognizer()

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


talk("Do you want to Type or Use Voice Command for the rest of the application?")
talk("Type '1' to use Keyboard Type and Type '2' to use Voice Command")
choice=input("Type '1' to use Keyboard Type and Type '2' to use Voice Command: ")
c=int(choice)
if c==1:

    talk("Enter the path of the PDF file to which you want to listen to")
    name=input("Enter the path of the PDF file to which you want to listen to: ")
    book=open(name,'rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    print("The PDF file contains: "+str(pages)+" pages")
    talk("The PDF file contains: "+str(pages)+" pages")
    talk("Enter the page number from which you want to start reading from")
    p_num=input("Enter the page number from which you want to start reading from: ")
    p_int=int(p_num)
    p=p_int-1
    page=pdfReader.getPage(p)
    text=page.extractText()
    talk("Do u want to see the text apart from reading it? Type '1' if Yes and Type '2' if No")
    i=input("Do u want to see the text apart from reading it? Type '1' if Yes and Type '2' if No: ")
    i_int=int(i)
    if i_int==1:
        print(text)
        talk(text)
        print("Your reading is completed!")
        talk("Your reading is completed!")
    elif i_int==2:
        talk(text)
        print("Your reading is completed!")
        talk("Your reading is completed!")
    else:
        print("Invalid Choice")

elif c==2:

    talk("Tell the path of the PDF file to which you want to listen to")
    talk("MAKE SURE THAT THE NAME OF YOUR PDF FILE IS IN SMALL LETTERS")
    name=get_info()
    book=open(name,'rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    print("The PDF file contains: "+str(pages)+" pages")
    talk("The PDF file contains: "+str(pages)+" pages")
    talk("Enter the page from which you want to start reading from: ")
    p_num=get_info()
    p_int=int(p_num)
    p=p_int-1
    page=pdfReader.getPage(p)
    text=page.extractText()
    talk("Do u want to see the text apart from reading it? Type '1' if Yes and Type '2' if No")
    i=input("Do u want to see the text apart from reading it? Type '1' if Yes and Type '2' if No: ")
    i_int=int(i)
    if i_int==1:
        print(text)
        talk(text)
        print("Your reading is completed!")
        talk("Your reading is completed!")
    elif i_int==2:
        talk(text)
        print("Your reading is completed!")
        talk("Your reading is completed!")
    else:
        print("Invalid Choice")
else:
    print("Invalid Choice")