import os.path
import os.path

import requests
import rumps
from bs4 import BeautifulSoup
from urllib3 import HTTPSConnectionPool

from url import *


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
        try:
            response = requests.get(url=URL + self.username + Rep)
            response.raise_for_status()
        except :
            rumps.alert("Network Error", "Check your network connection", ok=None, icon_path="gitIco.png")
            return ["error"]
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll("a", attrs={"itemprop": "name codeRepository"})
        return soup


getData = GetData()
print(getData.getRep())
