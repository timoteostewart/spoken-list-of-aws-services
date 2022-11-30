import pyttsx3

# initialize and configure TTS processor
pyttsx3_engine = pyttsx3.init()
pyttsx3_engine.setProperty(  # required by Windows
    "voice",
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
)


def save_text_to_mp3(text: str, mp3_full_path: str):
    try:
        pyttsx3_engine.save_to_file(text, mp3_full_path)
        pyttsx3_engine.runAndWait()
    except Exception as e:
        print(e)
