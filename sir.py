import pyttsx3
import webbrowser
import pyautogui
import time
import speech_recognition as sr

r = sr.Recognizer()



def listen():
   text = ""
   with sr.Microphone() as source:
       print("Listening....")
       audio = r.listen(source)
       try:
           text = r.recognize_google(audio)
           print(text)
       except:
           print("Could not understand")
           text = ""

   return text
def speak(text):
   i = pyttsx3.init()
   i.say(text)
   i.runAndWait()
  
  
while True:
   choice = listen().lower()
  
   if choice == "hi":
       print("Hello")
       speak("Hello ")
      
   elif choice == "good morning":
       print("Good Morning")
       speak("Good Morning")


   elif choice == "open google":
       print("Opening Google")
       speak("Opening Google")
       webbrowser.open("https://www.google.com")
      
   elif "search on youtube" in choice:
       topic = choice[17:]
       print("searching",topic,"on Youtube")
       speak("searching "+topic+" on Youtube")
       webbrowser.open("https://www.youtube.com/watch?v=5XXqDoYlc6A&list=RD5XXqDoYlc6A&start_radio=1&t=2s" +topic)
       print("Playing")
       time.sleep(2)
       pyautogui.moveTo(450,350)
       time.sleep(1)
       pyautogui.click()   
      
                
   elif "search on google" in choice:
       topic = choice[17:]
       print("searching",topic,"on Google")
       speak("searching "+topic+" on Google")
       webbrowser.open("https://www.google.com/search?q="+topic)
      
      
   elif choice == "open youtube":
       print("Opening Youtube")
       speak("Opening Youtube")
       webbrowser.open("https://www.youtube.com")
       break
      
      
   elif choice == "bye":
        
        print("Bye")
        speak("Bye")
        break
  
   else:
       print("Sorry Cant Understand")
       speak("Sorry Cant Understand")