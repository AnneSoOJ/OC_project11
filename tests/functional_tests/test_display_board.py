from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDisplayBoard:

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get("http://127.0.0.1:5000/showClubs")

    def tearDown(self):
        self.browser.close()

    def test_display_board(self):
        self.setUp()

        assert self.browser.find_element(By.TAG_NAME, 'h3').text, "Clubs:"

        self.tearDown()
