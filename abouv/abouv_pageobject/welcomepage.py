from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logger = logging.getLogger(__name__)



class welcome:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        self.sing_up = (By.XPATH, '/html/body/div/div/div[3]/div/div')
        self.skip_button = (By.XPATH, '//button[text()="Skip"]')
        self.phonenumber = (By.XPATH, '//input[@placeholder="Mobile Number"]')
        self.clickcontinue = (By.XPATH, '//button[@type="submit"]')
        self.otpmessage = (By.CSS_SELECTOR, 'body > section > ol > li > div:nth-child(2) > div')
        self.otpfeild = (By.XPATH, '(//input[@inputmode="text"])[1]')
        self.otpfeildsecond = (By.XPATH, '(//input[@inputmode="text"])[2]')
        self.otpfeildthired = (By.XPATH, '(//input[@inputmode="text"])[3]')
        self.otpfeildfourth = (By.XPATH, '(//input[@inputmode="text"])[4]')


    #Click the singup  button
    def singup(self):
        singup_botton = self.wait.until(EC.visibility_of_element_located(self.sing_up))
        singup_botton.click()
        logger.info("click singup button")

        try:
            skip_button = self.wait.until(EC.element_to_be_clickable(self.skip_button))
            skip_button.click()
            print("Skipped 'Install the app' popup")
        except Exception as e:
            print("No popup found or unable to skip: ", str(e))

 #Enter Phone Number

    def enterphonenumber(self, number):
        phonenumber_button = self.wait.until(EC.element_to_be_clickable(self.phonenumber))
        phonenumber_button.click()
        phonenumber_button.send_keys(number)

        # Log the phone number entered
        logger.info("Enter Phone number: %s", number)
        time.sleep(5)

        # Continue with the next step after the wait
        clickcontinue = self.wait.until(EC.element_to_be_clickable(self.clickcontinue))
        clickcontinue.click()

    def enter_otp(self):
        # Wait for and extract the OTP message
        otp_message = self.wait.until(EC.presence_of_element_located(self.otpmessage))
        time.sleep(3)
        otp_text = otp_message.text
        time.sleep(3)
        print("OTP message text:", otp_text)
        time.sleep(3)

        # Extract the OTP number from the message
        otp_number = otp_text.split()[-1]
        print("Extracted OTP number:", otp_number)
        time.sleep(3)

        # Locate all OTP input fields
        otp_fields = self.wait.until(EC.presence_of_element_located(self.otpfeild))
        otp_fieldssecond = self.wait.until(EC.presence_of_element_located(self.otpfeildsecond))
        otp_fieldsthired = self.wait.until(EC.presence_of_element_located(self.otpfeildthired))
        otp_fieldsfourth = self.wait.until(EC.presence_of_element_located(self.otpfeildfourth))

        # Input each OTP digit into its corresponding field
        otp_fields.send_keys(otp_number[0])
        time.sleep(1)
        otp_fieldssecond.send_keys(otp_number[1])
        time.sleep(1)
        otp_fieldsthired.send_keys(otp_number[2])
        time.sleep(1)
        otp_fieldsfourth.send_keys(otp_number[3])

        # Click the "Continue" button after entering the OTP
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
        continue_button.click()




