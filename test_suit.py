import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class suit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Selenium_Drivers\chromedriver.exe")

    def test_search(self):
        self.driver.get("http://www.google.com")
        self.search = self.driver.find_element_by_name("q")
        self.search.send_keys("selenium")
        time.sleep(1.5)
        self.search.submit()
        time.sleep(1.5)
        self.text = self.driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3")
        self.text.click()
        time.sleep(1.5)

    def test_selection(self):
        self.driver.get("http://www.w3schools.com")
        time.sleep(1.5)
        self.link = self.driver.find_element_by_link_text("Learn Python")
        self.link.click()
        time.sleep(1.5)
    
    def test_scroll(self):
        self.driver.get("https://www.amazon.com")
        self.search_amazon = self.driver.find_element_by_name("field-keywords")
        self.search_amazon.clear()
        self.search_amazon.send_keys("Games")
        self.search_amazon.send_keys(Keys.RETURN)
        time.sleep(1.5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1.5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Test Suit Results"))
