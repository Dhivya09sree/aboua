from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger(__name__)



class singup:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        self.hear = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]')
        self.clickcontinue = (By.XPATH, '//button[text()="Continue"]')
        self.role = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]')
        self.goal = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]')
        self.email = (By.XPATH, '//button[text()="Continue with email"]')
        self.inputemail = (By.XPATH, '//input[@type="email"]')
        self.youinputemail = (By.XPATH, '//*[@id="login"]')
   #select How did you hear about us
    def selecthear(self):
        selhear = self.wait.until(EC.element_to_be_clickable(self.hear))
        selhear.click()
        logger.info("select How did you hear about us?")

        # Continue with the next step after the wait
        clickcontinue = self.wait.until(EC.element_to_be_clickable(self.clickcontinue))
        clickcontinue.click()
    #Current Role?
    def curole(self):
        currentrole = self.wait.until(EC.element_to_be_clickable(self.role))
        time.sleep(5)
        currentrole.click()
        time.sleep(5)
        logger.info("select Current Role?")

        # Continue with the next step after the wait
        clickcontinue = self.wait.until(EC.element_to_be_clickable(self.clickcontinue))
        clickcontinue.click()
    #What's your goal?

    def cugoal(self):
        currentgoal = self.wait.until(EC.element_to_be_clickable(self.goal))
        time.sleep(5)
        currentgoal.click()
        time.sleep(5)
        logger.info("select Current Role?")

        # Continue with the next step after the wait
        clickcontinue = self.wait.until(EC.element_to_be_clickable(self.clickcontinue))
        clickcontinue.click()
    def chooseemail(self):
        gmail = self.wait.until(EC.element_to_be_clickable(self.email))
        time.sleep(5)
        gmail.click()
        time.sleep(5)
        logger.info("chosse email")

    def enteremail(self, email):
        email_button = self.wait.until(EC.element_to_be_clickable(self.inputemail))
        time.sleep(5)
        email_button.click()
        time.sleep(5)
        email_button.send_keys(email)

        # Log the phone number entered
        logger.info("Enter email : %s", email)
        # Continue with the next step after the wait
        clickcontinue = self.wait.until(EC.element_to_be_clickable(self.clickcontinue))
        clickcontinue.click()
        time.sleep(10)


        """
        self.driver.get("https://yopmail.com/en/")
        logger.info("Nagvigate To Email Site  : https://yopmail.com/en/wm")
        time.sleep(5)

        youemail_button = self.wait.until(EC.element_to_be_clickable(self.youinputemail))
        time.sleep(5)
        youemail_button.click()
        time.sleep(5)
        youemail_button.send_keys(email)
        youemail_button.send_keys(Keys.ENTER)

        """

