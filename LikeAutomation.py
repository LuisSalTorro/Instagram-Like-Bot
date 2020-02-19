from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def openInstagramAndLogin():
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(5)

    # locates email and password fields
    email = driver.find_element_by_name('username')
    passWord = driver.find_element_by_name('password')
    credentials = readFile()  # returns username and password in array

    # types username and password into fields
    email.send_keys(credentials[0])
    passWord.send_keys(credentials[1])
    passWord.send_keys(Keys.ENTER)  # hits enter button


def readFile():
    fileName = "./loginInfo.txt"
    return open(fileName).read().splitlines()


def searchBar():
    popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    popup.click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div').click() #click searchbar
    time.sleep(1)
    search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys("memes")
    search.send_keys(Keys.ENTER)


driver = webdriver.Firefox()
#functions
openInstagramAndLogin()
time.sleep(5)
searchBar()
# Following line is the HTML to move to the next post by clicking the next button
# <a class=" _65Bje  coreSpriteRightPaginationArrow" tabindex="0">Next</a>

# like button
# <svg aria-label="Like" class="_8-yf5 " fill="#262626" height="24" viewBox="0 0 48 48" width="24"><path clip-rule="evenodd" d="M34.3 3.5C27.2 3.5 24 8.8 24 8.8s-3.2-5.3-10.3-5.3C6.4 3.5.5 9.9.5 17.8s6.1 12.4 12.2 17.8c9.2 8.2 9.8 8.9 11.3 8.9s2.1-.7 11.3-8.9c6.2-5.5 12.2-10 12.2-17.8 0-7.9-5.9-14.3-13.2-14.3zm-1 29.8c-5.4 4.8-8.3 7.5-9.3 8.1-1-.7-4.6-3.9-9.3-8.1-5.5-4.9-11.2-9-11.2-15.6 0-6.2 4.6-11.3 10.2-11.3 4.1 0 6.3 2 7.9 4.2 3.6 5.1 1.2 5.1 4.8 0 1.6-2.2 3.8-4.2 7.9-4.2 5.6 0 10.2 5.1 10.2 11.3 0 6.7-5.7 10.8-11.2 15.6z" fill-rule="evenodd"></path></svg>
