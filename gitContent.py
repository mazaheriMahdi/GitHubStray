import rumps


class GitContentMeue(rumps.MenuItem):
    def __init__(self, title, type, date , href):
        super().__init__(title.title() + "\t\t" + date)
        self.href = href
        self.type = type
        self.date = date
