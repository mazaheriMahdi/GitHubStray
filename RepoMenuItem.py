import rumps
import webbrowser
URL_w = "https://github.com"

class MenuItem(rumps.MenuItem):
    def __init__(self , link , text):
        super().__init__(text)
        self.link = link
        self.set_callback(self.goTolink)
    def goTolink(self, _):
        webbrowser.open(url=URL_w+self.link)