import os
import time
import threading
import pyttsx3

from listener import listen
from parser import parse
from executor import run
from gui import TrayGUI
from notifier import notify


# ---------------- GLOBAL VARIABLES ---------------- #
wake_word = "system activate"
stop_cmd = "stop listening"

listening_state = False
running = True

# ----------- Text-To-Speech Engine ----------- #
tts = pyttsx3.init()
def speak(msg):
    try:
        tts.say(msg)
        tts.runAndWait()
    except:
        pass


# ---------------- VOICE LOOP ---------------- #
def voice_loop():
    global listening_state, running

    while running:
        # -------- WAITING (Not Listening) -------- #
        if not listening_state:
            text = listen()
            if text == wake_word:
                listening_state = True
                notify("Voice OS", "🎤 Listening Activated")
                speak("listening activated")
                print("[VOICE] Listening Activated")
            continue

        # -------- ACTIVE LISTENING -------- #
        text = listen()

        if text:
            print(f"[VOICE] Heard: {text}")

        if text == stop_cmd:
            listening_state = False
            notify("Voice OS", "🟡 Listening Stopped")
            speak("listening stopped")
            print("[VOICE] Listening Stopped")
            continue

        # Execute command
        action = parse(text)
        if action:
            print(f"[EXEC] Action: {action}")

        result = run(action)
        if result:
            speak(result)


# ---------------- TRAY CALLBACKS ---------------- #
def start_listening():
    global listening_state
    listening_state = True
    notify("Voice OS", "🎤 Listening Activated")
    speak("listening activated")
    print("[VOICE] Listening Activated (Manual)")


def stop_listening():
    global listening_state
    listening_state = False
    notify("Voice OS", "🟡 Listening Stopped")
    speak("listening stopped")
    print("[VOICE] Listening Stopped (Manual)")


def exit_app():
    global running
    running = False
    notify("Voice OS", "❌ Closing")
    speak("closing system")
    print("[SYSTEM] Exiting Voice OS")
    os._exit(0)


# ---------------- APP START ---------------- #
def main():
    global running

    print("[SYSTEM] Starting VoiceOS...")

    # Create tray GUI
    gui = TrayGUI(start_listening, stop_listening, exit_app)

    # Run tray in background thread
    threading.Thread(target=lambda: gui.run(), daemon=True).start()

    # Delay to let tray appear first
    time.sleep(1)

    # Start listening thread
    threading.Thread(target=voice_loop, daemon=True).start()

    notify("Voice OS", "🟢 System Started")
    speak("system started")
    print("[SYSTEM] Voice OS Started — Ready")

    # Keep app alive
    while running:
        time.sleep(1)


if __name__ == "__main__":
    main()
