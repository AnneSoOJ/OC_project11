from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSummary:

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get("http://127.0.0.1:5000/")

    def tearDown(self):
        self.browser.close()

    def test_logIn(self):
        self.setUp()

        email = self.browser.find_element(By.NAME, "email")
        email.send_keys("john@simplylift.co")

        login = self.browser.find_element(By.ID, "submit")
        login.click()
        self.browser.implicitly_wait(1)

        assert "Points available: 13" in self.browser.page_source
        assert self.browser.find_element(By.TAG_NAME, 'h3').text, "Competitions:"

        self.tearDown()
