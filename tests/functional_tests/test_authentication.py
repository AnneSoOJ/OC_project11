from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuthentication:

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get("http://127.0.0.1:5000/")

    def tearDown(self):
        self.browser.close()

    def test_logIn(self):
        self.setUp()

        email = self.browser.find_element(By.NAME, "email")
        email.send_keys("admin@irontemple.com")

        login = self.browser.find_element(By.ID, "submit")
        login.click()
        self.browser.implicitly_wait(1)

        assert self.browser.find_element(By.TAG_NAME, 'h2').text, "Welcome, admin@irontemple.com"

        self.tearDown()

    def test_logOut(self):
        self.setUp()

        email = self.browser.find_element(By.NAME, "email")
        email.send_keys("admin@irontemple.com")

        login = self.browser.find_element(By.ID, "submit")
        login.click()
        self.browser.implicitly_wait(1)

        assert self.browser.find_element(By.TAG_NAME, 'h2').text, "Welcome, admin@irontemple.com"
        assert self.browser.find_element(By.TAG_NAME, 'h3').text, "Competitions:"

        logout = self.browser.find_element(By.LINK_TEXT, "Logout")
        logout.click()
        self.browser.implicitly_wait(1)

        assert self.browser.find_element(By.TAG_NAME, 'h1').text, "Welcome to the GUDLFT Registration Portal!"

        self.tearDown()
