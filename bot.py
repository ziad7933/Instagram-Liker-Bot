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
        
    # def get_unfollowers(self):
    #     self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()

    # def like_photo(self, hashtag):
    #     driver = self.driver
    #     driver.get("https://www.instagram.com/explore/tags/"+ hashtag + "/")
    #     sleep(3)
    #     for i in range(1, 3):
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         sleep(2)
            
    #     hrefs = driver.find_elements_by_tag_name('a')
    #     pic_hrefs = [elem.get_attribute('href') for elem in hrefs]      #error with finding the names by 
    #     pic_hrefs = [href for href in pic_hrefs if hashtag in href]
    #     print(hashtag + ' photos: ' + str(len(pic_hrefs)))
        
    #     for pic_href in pic_hrefs:
    #         driver.get(pic_href)
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         try:
    #             driver.find_element_by_link_text("Like").click()
    #             sleep(10)
    #         except Exception as e:
    #             sleep(3)
    
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
        
        
        
my_bot = InstaBot("casejutsushop", "farhanziad420")
words = ['DCcomics', 'marvel', 'marvelcomics', 'demonslayer', 'abstract', 'comics', 'kakashi', 'Dabi', 'Deku', 'tokyoghoul', 'kanekiken', 'onepiece', 'luffy', 'luffyace', 'aceonepiece', 'zoro', 'sanji', 'attackontitan', 'shingekinokyojin', 'dragonballz', 'goku', 'levi']
for i in words:
    my_bot.like_photo(i)

