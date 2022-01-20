import speech_recognition as sr
import pyttsx3
import serial
import time


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


ser = serial.Serial("COM5")  # the port where your arduino board is


def run_wheelVC():
    command = take_command()
    print(command)
    if "start" in command:
        print("Spinning the wheels...")
        talk("Spinning the wheels...")
        time.sleep(1)
        ser.write(b'H')  # H means HIGH (bright)
        ser.close()
        exit()
    elif "stop" in command:
        print("Stopping the wheels...")
        talk("Stopping the wheels...")
        time.sleep(1)
        ser.write(b'L')  # L means LOW (dark)
        ser.close()
        exit()
    else:
        print("Please use run or stop")
        talk("Please use run or stop")


while True:
    run_wheelVC()
