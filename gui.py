import pystray
from PIL import Image, ImageDraw
from notifier import notify

class TrayGUI:
    def __init__(self, on_start, on_stop, on_exit):
        self.on_start = on_start
        self.on_stop = on_stop
        self.on_exit = on_exit

        self.idle_icon = self.make("gray")
        self.active_icon = self.make("green")

        self.icon = pystray.Icon("VoiceOS", self.idle_icon, "Voice OS Assistant")
        self.icon.menu = pystray.Menu(
            pystray.MenuItem("Start Listening", lambda: self.start()),
            pystray.MenuItem("Stop Listening", lambda: self.stop()),
            pystray.MenuItem("Exit", lambda: self.exit())
        )

    def make(self, color):
        img = Image.new("RGB", (64, 64), "white")
        d = ImageDraw.Draw(img)
        d.ellipse((16, 16, 48, 48), fill=color)
        return img

    def start(self):
        self.on_start()
        self.icon.icon = self.active_icon

    def stop(self):
        self.on_stop()
        self.icon.icon = self.idle_icon

    def exit(self):
        notify("Voice OS", "❌ Closing")
        self.icon.stop()
        self.on_exit()

    def run(self):
        self.icon.run()
