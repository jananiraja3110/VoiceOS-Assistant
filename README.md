# 🎤 VoiceOS – Offline Voice-Controlled Desktop Assistant

VoiceOS is a Python-based system assistant that listens to voice commands and controls your Windows computer — **without any AI models or internet**.  
It works fully offline using CMU PocketSphinx and can open apps, search, control Windows actions like shutdown, restart, volume, and much more.

---

## 🚀 Features

| Category | Capabilities |
|----------|--------------|
| 🎙 Voice Trigger | Wake word (`system activate`), stop (`stop listening`) |
| 🧠 Offline | Speech recognition (no internet) |
| 🪟 System Control | Shutdown, restart, mute, volume, minimize |
| 📂 App Launching | Chrome, Word, Excel, File Explorer |
| 🌐 Browser | Google search, YouTube, ChatGPT |
| 🧱 Tray Mode | Runs silently in background |
| 🧾 Windows EXE | Can be packaged to `.exe` |

---

## 🏗️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| Speech Engine | CMU PocketSphinx |
| Audio | PyAudio |
| GUI / Tray | PyStray |
| System Actions | OS, subprocess, pyautogui |
| Packaging | PyInstaller |

---

## 📁 Folder Structure

voice_os_control/
│── main.py
│── listener.py
│── parser.py
│── executor.py
│── gui.py
│── notifier.py
│── config/
│ ├── commands.json
│ └── app_paths.json
│── assets/
│ └── icon.ico
│── requirements.txt


---

## 🧰 Setup & Installation

```bash
git clone https://github.com/YOUR_USERNAME/VoiceOS-Assistant.git
cd VoiceOS-Assistant
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python main.py

🧾 Run Commands (Speak)

| Say This               | What Happens               |
| ---------------------- | -------------------------- |
| `system activate`      | Enable listening mode      |
| `stop listening`       | Disable voice command mode |
| `open chrome`          | Launch Chrome              |
| `open whatsapp`        | Opens WhatsApp Web         |
| `open file explorer`   | Opens Windows Explorer     |
| `search python course` | Google search              |
| `shutdown laptop`      | Shutdown                   |
| `restart laptop`       | Restart                    |



