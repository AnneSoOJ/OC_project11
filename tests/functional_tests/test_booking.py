from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBooking:

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get("http://127.0.0.1:5000/")

    def tearDown(self):
        self.browser.close()

    def test_booking(self):
        self.setUp()

        email = self.browser.find_element(By.NAME, "email")
        email.send_keys("kate@shelifts.co.uk")

        login = self.browser.find_element(By.ID, "submit")
        login.click()
        self.browser.implicitly_wait(1)

        book = self.browser.find_element(By.LINK_TEXT, "Book Places")
        book.click()
        self.browser.implicitly_wait(1)

        places = self.browser.find_element(By.NAME, "places")
        self.browser.implicitly_wait(1)
        places.send_keys("3")
        self.browser.implicitly_wait(1)

        booking = self.browser.find_element(By.NAME, "book")
        booking.click()
        self.browser.implicitly_wait(1)

        assert self.browser.find_element(By.TAG_NAME, 'h2').text, "Welcome, kate@shelifts.co.uk"
        assert self.browser.find_element(By.TAG_NAME, 'h3').text, "Competitions:"

        self.tearDown()
