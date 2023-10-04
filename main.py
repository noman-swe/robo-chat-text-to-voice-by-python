import win32com.client as wincom

if __name__ == '__main__':
    print("Welcome to RoboSpeaker, Created by Noman")

    while True:
        x = input("Enter what you want me to speak :")
        if x == "khamosh":
            khamoshText = "thanks for this happy conversation. see you later"
            print(khamoshText)
            speak = wincom.Dispatch("SAPI.SpVoice")
            speak.Speak(khamoshText)
            break

        speak = wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(x)

