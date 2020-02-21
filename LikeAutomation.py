from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LikeAutomation(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.openAndLogin()

    def openAndLogin(self):
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(5)
        # locates email and password fields
        email = self.driver.find_element_by_name('username')
        passWord = self.driver.find_element_by_name('password')
        credentials = self.readFile("./loginInfo.txt")  # returns username and password in array
        # types username and password into fields
        email.send_keys(credentials[0])
        passWord.send_keys(credentials[1])
        passWord.send_keys(Keys.ENTER)  # hits enter button

    def readFile(self, fileName):
        return open(fileName).read().splitlines()

    def searchBar(self, tagToSearch):
        time.sleep(4)
        self.driver.get('https://www.instagram.com/explore/tags/' + tagToSearch)
        time.sleep(5)

    def likePosts(self, amountOfLikes, timeInbetween):
        # opens a post
        self.driver.find_elements_by_class_name('v1Nh3')[9].click()  # [9] likes recent posts [0] likes most popular
        time.sleep(6)
        i = 0

        while i <= amountOfLikes:
            try:
                # likes post
                like = self.driver.find_element_by_class_name('wpO6b')
                like.click()
                time.sleep(1)
                # moves to next post
                next = self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                next.click()
            except Exception:
                #XPath /html/body/div[4]/div[1]/div/div/a[2]
                self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i += 1
            print(i) #kinda like a console.log to check how often we liked an image in case there are any uncaught errors
            time.sleep(timeInbetween)
        #goes to meme's section to signal that the bot is finished
        self.driver.get('https://www.instagram.com/explore/tags/memes')
        return i
