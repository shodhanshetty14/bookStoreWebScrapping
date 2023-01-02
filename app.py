from selenium import webdriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class SapnaOnline:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get('https://www.sapnaonline.com/shop/fiction/')
        self.driver.implicitly_wait(5)


    def fict_novel(self):
        BookLinks = []
        booksBox = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div')
        bookTags = booksBox.find_elements(By.TAG_NAME, 'a')
        for tag in bookTags:
            link = tag.get_attribute('href')
            if link in BookLinks:
                continue
            elif "/books/" in link:
                BookLinks.append(link)
        # print(BookLinks)
        return BookLinks


    def book_details(self, books):
        data = {}
        for book in books:
            self.driver.get(book)
            
            image = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/img[2]").get_attribute('src')
            data['image'] = image
            
            title = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/div[2]/h1").text
            data['title'] = title
            
            price = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").text
            data['price'] = price
            
            description = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div/span").text
            data['description'] = description
            
            print(data)


def postReq(data):
    pass




if __name__ == '__main__':
    bot = SapnaOnline()
    books = bot.fict_novel()
    bot.book_details(books)