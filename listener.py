import speech_recognition as sr

MIC_INDEX = 3  # your mic index (Realtek)

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=MIC_INDEX) as src:
            print("[MIC] Listening...")
            r.adjust_for_ambient_noise(src, duration=0.4)
            audio = r.listen(src, timeout=3, phrase_time_limit=4)
            text = r.recognize_sphinx(audio).lower()
            print("[MIC] Detected:", text)
            return text
    except Exception as e:
        print("[MIC ERROR]", e)
        return ""
