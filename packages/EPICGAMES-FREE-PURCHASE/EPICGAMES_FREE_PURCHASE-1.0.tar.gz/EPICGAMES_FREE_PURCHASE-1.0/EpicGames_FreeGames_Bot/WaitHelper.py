from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
class WaitHelper:
    @staticmethod
    def wait_for_element(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    @staticmethod
    def wait_for_elements(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located((by, value)))

    @staticmethod
    def random_sleep(min_sleep, max_sleep):
        random_sleep_duration = random.uniform(min_sleep, max_sleep)
        time.sleep(random_sleep_duration)