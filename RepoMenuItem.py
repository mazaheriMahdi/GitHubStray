import webbrowser
from data import GetData
import rumps

URL_w = "https://github.com"


class MenuItem(rumps.MenuItem):
    def __init__(self, link, text):
        super().__init__(text)
        self.text = text
        self.link = link
        self.set_callback(self.goTolink)
        data = GetData()
        for i in data.getRepoContent(name=self.text.strip()):
            self.add(i)
    def goTolink(self, _):
        webbrowser.open(url=URL_w + self.link)
