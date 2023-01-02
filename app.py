from selenium import webdriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class SapnaOnline:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.sapnaonline.com/shop/fiction/')
        self.driver.implicitly_wait(5)
        print('hello')


    def fict_novel(self):
        print('hey')
        # bookCards = self.driver.find_elements(By.CSS_SELECTOR, 'div.CategoryTabInner__ProductBox-qaa80s-0 > div')
        # for card in bookCards:
        print('hello')
        imageLink = self.driver.find_element(By.CLASS_NAME, 'bookImage').get_attribute('src')
        
        bookName = self.driver.find_element(By.CLASS_NAME, 'ProductCard__AboutText-sc-10n3822-2 kOZyab link').text
        
        authorName = self.driver.find_element(By.CLASS_NAME, 'ProductCard__AuthorText-sc-10n3822-4 cZBirR').text
        
        print(imageLink, bookName, authorName)
        self.driver.quit()


def postReq(data):
    pass




if __name__ == '__main__':
    bot = SapnaOnline()
    bot.fict_novel()
