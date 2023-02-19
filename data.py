import os.path
import os.path

import requests
import rumps
from bs4 import BeautifulSoup

import url
from gitContent import GitContentMeue
from url import *


class GetUserName(rumps.Window):
    def __init__(self):
        super().__init__("Your GitHub user name ", "Config")
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
        except:
            rumps.alert("Network Error", "Check your network connection", ok=None, icon_path="gitIco.png")
            return ["error"]
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll("a", attrs={"itemprop": "name codeRepository"})
        return soup

    def getRepoContent(self, name):

        try:
            response = requests.get(url=url.URL + self.username + "/" + name)
            soup = BeautifulSoup(response.text, "html.parser")
            soup = soup.findAll("div", role="row", class_="Box-row--focus-gray")

        except:
            rumps.alert("Network Error", "Check your network connection", ok=None, icon_path="gitIco.png")
            return ["error"]
        finally:
            list = []
            for i in soup:
                list.append(GitContentMeue(i.find_next("a", class_="js-navigation-open Link--primary")['title'],
                                           i.find_next("svg")["aria-label"], ""))
            return list
#
# getData = GetData()
# print(getData.getRepoContent("puzzle"))
