import speech_recognition as sr
import pyttsx3
import sys
from PyDictionary import PyDictionary


r = sr.Recognizer()


print("The program has started...")

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    #engine.setProperty('voice', voices[1].id) 
    engine.say(audio)
    engine.runAndWait()

def meaning(word):
    dictionary1 = PyDictionary()
    meaning = dictionary1.meaning(word)
    print(meaning)

    if meaning is not None:
        completeMeaning = ''
        for key in meaning:
            (key, '->', speak(meaning[key][0]))
    
    return ''

def translateInHindi(word):
    print("The word for the translation is " + word)
    dictionary = PyDictionary()
    inHindi = dictionary.translate(word,'hi')
    print(inHindi)
    return inHindi

with sr.Microphone() as source:
    while True: 
        print("Silence please, calibrating background noise")
        r.adjust_for_ambient_noise(source, 1)
        print("Calibrated!.. Say something now")
        audio = r.listen(source)

        try:
            instruction = r.recognize_google(audio)
            print("You said: " + instruction)

            if 'there' in instruction:
                speak("Yes sir")

            if  'off' in instruction:
                speak("Turning off the program")
                sys.exit()

            if 'meaning' in instruction:
                instruction = instruction.replace('meaning of', '')
                print("Instruction after replacement " + instruction)
                word =  meaning(instruction)
                # speak("the meaning of word is ")
                #speak(word)
                # inHindi = translateInHindi(instruction)
                #  speak(inHindi)

            print('The program is completed')
            
        except sr.UnknownValueError as err:
            print("Hemant Speech Recognition could not understand audio; {0}".format(err))
            #speak("Sorry")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

 

