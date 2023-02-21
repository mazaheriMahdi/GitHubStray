import time
from threading import Thread

import rumps

from RepoMenuItem import MenuItem
from data import GetData

REFRESH = rumps.MenuItem("Refresh", icon="refresh.png")
USERNAME = rumps.MenuItem("Change user name", icon="username.png")
SHOW_ACCOUNT_INFO = rumps.MenuItem("Your account info", icon="gitIco.png")
YOUR_REPOSITORY = rumps.MenuItem("Your repository's : ")
MADE_WITH_LOVE = rumps.MenuItem("               MADE WITH ❤️ BY MAHDI MAZAHERI               ")


class AwesomeStatusBarApp(rumps.App):

    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")
        self.getData = GetData()
        self.icon = "gitIco.png"
        self.menu = [REFRESH, None, USERNAME, None, YOUR_REPOSITORY]
        self.quit_button = None

        t1 = Thread(target=self.initialMenuItem)
        t1.start()

        t2 = Thread(target=self.loading_animmation, args=[t1])
        t2.start()


        self.downloadingInformer()

    def create_thread(self, task, *args):
        return Thread(target=task, args=args)


    @rumps.clicked("Refresh")
    def refresh(self, _):
        t1 = Thread(target=self.initialMenuItem)
        t1.start()

        t2 = Thread(target=self.loading_animmation, args=[t1])
        t2.start()

    def downloadingInformer(self):
        rumps.alert("Loading", "Downloading Data from GitHub")

    def loading_animmation(self, threed):
        loading_string = "Loading..."
        self.icon = "reload.png"
        while threed.is_alive():

            temp = ""
            for i in loading_string:
                time.sleep(0.5)
                temp += i
                self.title = temp

        self.title = None
        self.icon = "gitIco.png"

    def initialMenuItem(self):
        self.menu.clear()
        self.menu = [REFRESH, None, USERNAME, None, YOUR_REPOSITORY]
        self.getRepoMeny()
        self.menu.add(None)
        self.menu.add(MADE_WITH_LOVE)
        self.menu.add(None)
        self.menu.add(rumps.MenuItem("Quit"))

    def getRepoMeny(self):
        repoList = self.getData.getRep()
        for item in repoList:
            menuItem = MenuItem(text=item.text.title(), link=item["href"])
            self.menu.add(menuItem)

    @rumps.clicked("Change user name")
    def change(self, _):
        self.getData.username = self.getData.getUserName()
        self.getData.saveUserName(self.getData.username)
        self.refresh(self)

    @rumps.timer(interval=60 * 9)
    def reGet(self, sender):
        """ Timer """

        def counter(t):
            self.refresh
            print("hello")

        counter(None)


if __name__ == "__main__":
    AwesomeStatusBarApp().run()
