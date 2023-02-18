import rumps

from RepoMenuItem import MenuItem
from data import GetData

REFRESH = rumps.MenuItem("Refresh", icon="refresh.png")
USERNAME = rumps.MenuItem("Change user name", icon="gitIco.png")
SHOW_ACCOUNT_INFO = rumps.MenuItem("Your account info", icon="gitIco.png")
YOUR_REPOSITORY = rumps.MenuItem("your repository's")
MADE_WITH_LOVE = rumps.MenuItem("MADE WITH ❤️ BY MAHDI MAZAHERI")


class AwesomeStatusBarApp(rumps.App):

    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")
        self.getData = GetData()
        self.title = f"Followers : {self.getData.getFollowers()}"
        self.icon = "gitIco.png"
        self.initialMenuItem()

    @rumps.clicked("Refresh")
    def refresh(self, _):
        self.title = f"Followers : {self.getData.getFollowers()}"
        self.menu.clear()
        self.initialMenuItem()

    def initialMenuItem(self):
        self.menu = [REFRESH, USERNAME, YOUR_REPOSITORY]
        self.getRepoMeny()
        self.menu.add(MADE_WITH_LOVE)

    def getRepoMeny(self):
        repoList = self.getData.getRep()
        for item in repoList:
            menuItem = MenuItem(text=item.text, link=item["href"])
            self.menu.add(menuItem)

    @rumps.clicked("Change user name")
    def change(self, _):
        self.getData.username = self.getData.getUserName()
        self.getData.saveUserName(self.getData.username)
        self.refresh()

    @rumps.timer(interval=60 * 2)
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
