import os, subprocess, pyautogui, json, webbrowser

def run(action):
    if action is None:
        return "command not found"

    if action == "OPEN_CHATGPT":
        webbrowser.open("https://chat.openai.com")
        return "opening chat g p t"

    if action.startswith("APP:"):
        app = action.split(":")[1]
        with open("config/app_paths.json") as f:
            apps = json.load(f)
        subprocess.Popen(apps[app])
        return f"opening {app}"
    
    import os, subprocess, pyautogui, json, webbrowser

def run(action):
    if not action: return "command not found"

    # --- Web actions
    if action.startswith("WEB:"):
        target = action.split(":")[1]
        if target == "whatsapp":
            webbrowser.open("https://web.whatsapp.com")
        elif target == "youtube":
            webbrowser.open("https://youtube.com")
        return f"opening {target}"

    # --- System Actions
    if action.startswith("SYS:"):
        sys = action.split(":")[1]
        if sys == "shutdown": os.system("shutdown /s /t 1")
        if sys == "restart": os.system("shutdown /r /t 1")
        if sys == "mute": pyautogui.press("volumemute")
        if sys == "volup": pyautogui.press("volumeup")
        if sys == "voldown": pyautogui.press("volumedown")
        if sys == "explorer": subprocess.Popen("explorer")
        return "done"

    # --- Application Open
    if action.startswith("APP:"):
        app = action.split(":")[1]
        with open("config/app_paths.json") as f:
            apps = json.load(f)
        subprocess.Popen(apps[app])
        return f"opening {app}"

    return None


    if action.startswith("SYS:"):
        c = action.split(":")[1]

        if c == "minimize": pyautogui.hotkey("win","down")
        if c == "lock": os.system("rundll32.exe user32.dll,LockWorkStation")
        if c == "camera": subprocess.Popen("start microsoft.windows.camera:", shell=True)

        return "done"

    return None
