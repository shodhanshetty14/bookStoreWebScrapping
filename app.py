from selenium import webdriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SapnaOnline:
    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.sapnaonline.com/shop/fiction/')
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 20)


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
        return BookLinks


    def book_details(self, books):
        data = {}
        for book in books:
            self.driver.get(book)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/img[2]")))
            
            image = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/img[2]").get_attribute('src')
            data['image'] = image
            
            title = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/div[2]/h1").text
            data['title'] = title
            
            author = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/div[3]/div[1]/div[1]/a").text
            data['author'] = author
            
            price = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").text
            data['price'] = price
            
            description = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div/span").text
            data['description'] = description
            
            isbn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/span[2]").text
            data['ISBN-13'] = isbn
            
            publisher = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[4]/div/span[2]").text
            data['publisher'] = publisher
            
            pubDate = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/span[2]").text
            data['publish date'] = pubDate
            
            print(data,'\n')
        self.driver.close()


def postReq(data):
    pass




if __name__ == '__main__':
    bot = SapnaOnline()
    books = bot.fict_novel()
    bot.book_details(books)