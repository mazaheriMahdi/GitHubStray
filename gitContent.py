import rumps


class GitContentMeue(rumps.MenuItem):
    def __init__(self, title, type, date):
        super().__init__(title + "\t\t" + date)
        self.type = type
        self.date = date


