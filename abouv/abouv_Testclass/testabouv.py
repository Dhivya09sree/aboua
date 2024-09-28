import logging
import pytest
from selenium import webdriver
from abouv_pageobject.welcomepage import welcome
from abouv_pageobject.hearpage import singup
import time

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('test_login.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class TestLoginPage:
    BASE_URL = "https://sg-app.abouv.com/welcome"

    @pytest.fixture
    def setup(self):
        logger.info("Setting up WebDriver instance")
        driver = webdriver.Chrome()
        yield driver
        logger.info("Tearing down WebDriver instance")
        driver.quit()


    def test_login(self, setup):
        logger.info("Welcome Page")

        self.driver = setup
        self.driver.get(self.BASE_URL)
        logger.info(f"Navigated to {self.BASE_URL}")

        welcomepage = welcome(self.driver)

        welcomepage.singup()
        logger.info("click singup button")

        self.driver.maximize_window()
        logger.info("maximize_window")

        welcomepage.enterphonenumber(8807555547)# each time excuation change the phone number 
        logger.info("Enter the Phone number")

        welcomepage.enter_otp()
        logger.info("Enter the OTP in Page")


        singuppage = singup(self.driver)

        singuppage.selecthear()
        logger.info("Select how to hear me")
        time.sleep(10)
        singuppage.curole()
        logger.info("Select the role")
        time.sleep(10)
        singuppage.cugoal()
        logger.info("Select the goal")
        time.sleep(10)
        singuppage.chooseemail()
        logger.info("Choose the email")
        time.sleep(10)
        singuppage.enteremail("dhivya4@gmail.com")
        logger.info("Enter the Email")
        time.sleep(10)












