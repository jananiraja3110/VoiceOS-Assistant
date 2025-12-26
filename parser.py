import json
import webbrowser

def parse(text):
    text = text.lower().strip()

    if text.startswith("search "):
        q = text.replace("search ", "")
        webbrowser.open(f"https://www.google.com/search?q={q}")
        return f"searching {q}"

    if text.startswith("youtube "):
        q = text.replace("youtube ", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
        return f"opening youtube for {q}"

    if "open chatgpt" in text:
        return "OPEN_CHATGPT"

    if "minimize window" in text:
        return "SYS:minimize"

    if "lock screen" in text:
        return "SYS:lock"

    if "open camera" in text:
        return "SYS:camera"
    
    if "open word" in text:
        return "APP:word"

    if "open excel" in text:
        return "APP:excel"

    if "open file explorer" in text:
        return "SYS:explorer"

    if "open whatsapp" in text:
        return "WEB:whatsapp"

    if "open youtube" in text:
        return "WEB:youtube"

    if "shutdown" in text:
        return "SYS:shutdown"

    if "restart" in text:
        return "SYS:restart"

    if "mute" in text:
        return "SYS:mute"

    if "increase volume" in text:
        return "SYS:volup"

    if "decrease volume" in text:
        return "SYS:voldown"

    try:
        with open("config/commands.json") as f:
            d = json.load(f)
        if text in d: return d[text]
    except:
        pass

    return None
