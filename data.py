import os.path
import os.path
from url import  *
import requests
import rumps
from bs4 import BeautifulSoup


class GetUserName(rumps.Window):
    def __init__(self):
        super().__init__("Your GitHub user name ", "Config", "like mahdi83mazaheri ... ")
        self.icon = "gitIco.png"


class GetData:
    def __init__(self):
        # chech if there is data file or not
        if not self.isThereFile():
            # get username via rumps window
            self.saveUserName(self.getUserName())
        self.username = self.readDate()

    def isThereFile(self):
        return os.path.exists("data.txt")

    def readDate(self):
        with open("data.txt") as file:
            return file.read()

    def saveUserName(self, username):
        with open("data.txt", "w") as file:
            file.write(username)

    def getFollowers(self):
        response = requests.get("https://github.com/" + self.username)
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll("span", "text-bold color-fg-default")[0]
        return soup.text

    def getFollowing(self):
        response = requests.get("https://github.com/" + self.username)
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll("span", "text-bold color-fg-default")[1]
        return soup.text

    def getUserName(self):
        getUser = GetUserName()
        res = getUser.run()
        return res.text

    def getRep(self):
        response = requests.get(url=URL + self.username + Rep)
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll("a" , attrs={"itemprop":"name codeRepository"})

        return soup


getData = GetData()
print(getData.getRep())