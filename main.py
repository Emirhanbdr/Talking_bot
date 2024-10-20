import pyttsx3

engine=pyttsx3.init()

#for voice in engine.getProperty('voices'):
    #print(voice) ses listesi arandı
rate=150
engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga")
engine.setProperty("rate",rate)
text="Merhaba Atıl hocam seviliyorsunuz."
engine.say(text)
engine.runAndWait()
