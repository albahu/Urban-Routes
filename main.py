from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestMyWebPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Aumenté el tiempo de espera

    def run_tests(self):
        self.test_open_page()
        self.test_set_window_size()
        self.complete_booking_process()

    def test_open_page(self):
        self.driver.get("https://c8941e92-9b83-49d7-8de0-fc13b9f8c661.serverhub.tripleten-services.com?lng=es")

    def test_set_window_size(self):
        self.driver.set_window_size(1920, 1057)

    def test_click_from(self):
        self.wait_and_click(By.ID, "from")

    def test_set_from(self):
        self.driver.find_element(By.ID, "from").send_keys("east 2nd street 601")

    def test_click_to(self):
        self.wait_and_click(By.ID, "to")

    def test_set_to(self):
        self.driver.find_element(By.ID, "to").send_keys("1300 1st st")

    def test_click_personal(self):
        self.wait_and_click(By.CSS_SELECTOR, ".mode:nth-child(3)")

    def test_click_button_taxi(self):
        self.wait_and_click(By.CSS_SELECTOR, ".button:nth-child(3)")

    def test_click_comfort(self):
        self.wait_and_click(By.CSS_SELECTOR, ".tcard:nth-child(5) > .tcard-icon > img")

    def test_click_phone_button(self):
        self.wait_and_click(By.CSS_SELECTOR, ".np-text")

    def test_click_phone_number(self):
        self.wait_and_click(By.CSS_SELECTOR, ".active .label")

    def test_phone_input(self):
        self.driver.find_element(By.ID, "phone").send_keys("+1 123 123 12 12")

    def test_click_next(self):
        self.wait_and_click(By.CSS_SELECTOR, ".active .button")

    def test_click_close(self):
        self.wait_and_click(By.CSS_SELECTOR, ".active:nth-child(2) > .close-button")

    def test_click_comment_field(self):
        self.wait_and_click(By.CSS_SELECTOR, "div:nth-child(3) > .input-container > .label")

    def test_type_comment_field(self):
        self.driver.find_element(By.ID, "comment").send_keys("muestrame el camino al museo")

    def test_click_tissues(self):
        self.wait_and_click(By.CSS_SELECTOR, ".r:nth-child(1) .slider")

    def test_click_ice_cream(self):
        self.wait_and_click(By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus")

    def test_click_ice_cream_2(self):
        self.wait_and_click(By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus")

    def test_click_call_taxi_button(self):
        self.wait_and_click(By.CSS_SELECTOR, ".smart-button-main")

    def complete_booking_process(self):
        self.test_click_from()
        self.test_set_from()
        self.test_click_to()
        self.test_set_to()
        self.test_click_personal()
        self.test_click_button_taxi()
        self.test_click_comfort()
        self.test_click_phone_button()
        self.test_click_phone_number()
        self.test_phone_input()
        self.test_click_next()
        self.test_click_close()
        self.test_click_comment_field()
        self.test_type_comment_field()
        self.test_click_tissues()
        self.test_click_ice_cream()
        self.test_click_ice_cream_2()
        self.test_click_call_taxi_button()

    def wait_and_click(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            ActionChains(self.driver).move_to_element(element).click().perform()
        except TimeoutException:
            print(f"Timeout al esperar que el elemento {by}: {value} sea clickeable.")
            # Puedes agregar más manejo de errores aquí según sea necesario

if __name__ == "__main__":
    driver = webdriver.Chrome()
    test_instance = TestMyWebPage(driver)

    try:
        test_instance.run_tests()
    finally:
        time.sleep(5)
        driver.quit()
