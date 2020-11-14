from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(5)
    
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    sleep(1)
            except Exception as e:
                sleep(2)
            unique_photos -= 1
        
        
        
my_bot = InstaBot("username", "password")       # put your instagram username and password in the following fields.
words = ['Hashtag', 'Hashtag', 'Hashtag']       # type in the tags without the hashtag symbol inside the apostrophes. For example, 'abstract', 'sky', 'photography' etc.
for i in words:
    my_bot.like_photo(i)

