import os.path
import os.path

import requests
import rumps
from bs4 import BeautifulSoup

import url
from gitContent import GitContentMeue
from url import *


class GetUserName(rumps.Window):
    """A dialog which contain a text input for getting username"""

    def __init__(self):
        super().__init__("Your GitHub user name ", "Config")
        self.icon = "gitIco.png"


class GetData():
    """Get data from Git"""

    def __init__(self):
        # chech if there is data file or not
        if not self.isThereFile():
            # get username via rumps window
            self.saveUserName(self.getUserName())
        self.username = self.readDate()

    def isThereFile(self):
        """chech if the userName saved or not"""
        return os.path.exists("data.txt")

    def readDate(self):
        """Get username from .txt file."""
        with open("data.txt") as file:
            return file.read()

    def saveUserName(self, username):
        """save username to .txt file"""
        with open("data.txt", "w") as file:
            file.write(username)

    def getFollowers(self):
        """Get followers count from Git"""
        response = requests.get("https://github.com/" + self.username)
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll("span", "text-bold color-fg-default")[0]
        return soup.text

    def getFollowing(self):
        """Get following count from Git"""
        response = requests.get("https://github.com/" + self.username)
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll("span", "text-bold color-fg-default")[1]
        return soup.text

    def getUserName(self):
        """Get username from user"""
        getUser = GetUserName()
        res = getUser.run()
        return res.text

    def getRep(self):

        """Get user repositorys name"""
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
        """Get repository Contents"""

        try:
            response = requests.get(url=url.URL + self.username + "/" + name)
            soup = BeautifulSoup(response.text, "html.parser")
            soup = soup.findAll("div", role="row", class_="Box-row--focus-gray")

        except:
            return "error"
        finally:
            list = []
            for i in soup:
                a = i.find_next("a", class_="js-navigation-open Link--primary")
                list.append(GitContentMeue(a['title'],
                                           i.find_next("svg")["aria-label"], "", a["href"]))
            return list
# getData = GetData()
# t1 = Thread(target=getData.getRepoContent , args=["name"])
# t1.start()
# def monitor(thread):
#     while thread.is_alive():
#         time.sleep(0.1)
#         print("loading.")
#     print()
# t2 = Thread(target=monitor , args=[t1])
# t2.start()
