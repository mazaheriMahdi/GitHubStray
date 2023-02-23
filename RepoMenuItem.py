import webbrowser

import rumps

from data import GetData

URL_w = "https://github.com"


class MenuItem(rumps.MenuItem):
    def __init__(self, link, text, is_sub=False):
        super().__init__(text)
        self.is_sub = is_sub
        self.text = text
        self.link = link
        self.set_callback(self.goTolink)
        if not is_sub:
            data = GetData()
            repContent = data.getRepoContent(name=self.text.strip())
            if repContent != "error":
                for i in repContent:
                    newMenu = MenuItem(link=i.href, text=i.title, is_sub=True)
                    if i.type == "Directory":
                        newMenu.icon = "folder.png"
                    else:
                        newMenu.icon = "file.png"
                    self.add(newMenu)


    def goTolink(self, _):
        """Open menu Item link in browser."""
        webbrowser.open(url=URL_w + self.link)
