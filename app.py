from threading import Thread

import rumps

from RepoMenuItem import MenuItem
from data import GetData

REFRESH = rumps.MenuItem("Refresh", icon="refresh.png")
USERNAME = rumps.MenuItem("Change user name", icon="username.png")
SHOW_ACCOUNT_INFO = rumps.MenuItem("Your account info", icon="gitIco.png")
YOUR_REPOSITORY = rumps.MenuItem("Your repository's : ")
MADE_WITH_LOVE = rumps.MenuItem("MADE WITH ❤️ BY MAHDI MAZAHERI")


class AwesomeStatusBarApp(rumps.App):

    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")
        self.getData = GetData()
        self.icon = "gitIco.png"
        self.menu = [REFRESH, None, USERNAME, None, YOUR_REPOSITORY]
        self.quit_button = None
        t1 = Thread(target=self.initialMenuItem)
        t1.start()

    @rumps.clicked("Refresh")
    def refresh(self, _):
        self.title = f"Followers : {self.getData.getFollowers()}"
        self.menu.clear()
        self.initialMenuItem()

    def initialMenuItem(self):
        self.icon = "reload.png"
        self.title = "Loading.."
        self.menu.clear()

        self.menu = [REFRESH, None, USERNAME, None, YOUR_REPOSITORY]
        # al =rumps.alert(title="Loading..." , message="Data is loading please wait.." , ok=None , cancel=None , other=None)
        self.getRepoMeny()
        # t1 = Thread(target=)
        # t1.start()

        self.menu.add(None)
        self.menu.add(MADE_WITH_LOVE)
        self.menu.add(None)
        self.icon = "gitIco.png"
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

        # sender = self.menu['Air!']  # if action no bind on clicked action

        def counter(t):
            self.refresh
            print("hello")

        # if bind on clicked action
        # set_timer = rumps.Timer(callback=counter, interval=60 * 60)
        # set_timer.start()

        counter(None)


if __name__ == "__main__":
    AwesomeStatusBarApp().run()
