# imported packages for Testdata and Test locators in Test_imdb class

from TestData.ImdbData import Imdbdata
from Testlocators.ImdbLocators import Imdblocators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import pytest


class Test_Imdb:

    @pytest.fixture
    # booting function to run before all pytest
    def booting_fun(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield
        self.driver.close()

    def test_search_name_Birthdate(self, booting_fun):
        try:
            wait = WebDriverWait(self.driver, 10)
            self.driver.get(Imdbdata().url)
            self.driver.execute_script('window.scrollBy(0, 500)')
            # use of explict wait that wait till selenium get element clickable
            name = wait.until(EC.element_to_be_clickable((By.XPATH, Imdblocators().name_locator)))
            name.click()
            # use of explict wait ,once element is located
            search_box = wait.until(EC.presence_of_element_located((By.XPATH, Imdblocators().name_search_box_locator)))

            search_box.send_keys(Imdbdata().search_data)
            Birth_date = wait.until(EC.element_to_be_clickable((By.XPATH, Imdblocators().Birth_date_locator)))
            Birth_date.click()
            # use of explict wait that wait till selenium get element located
            start_date = wait.until(EC.presence_of_element_located((By.XPATH, Imdblocators().start_date_locator)))
            start_date.send_keys(Imdbdata().start_date)

            end_date = wait.until(
                EC.presence_of_element_located((By.XPATH, Imdblocators().end_date_locator)))
            end_date.send_keys(Imdbdata().end_date)
            result_box = wait.until(EC.element_to_be_clickable((By.XPATH, Imdblocators().result_locator)))
            result_box.click()
            # store text in variable name
            actor_name = self.driver.find_element(By.XPATH, value=Imdblocators().actor_locator).text
            # assert statement to verify expected result
            assert actor_name.replace("1. ", "") == Imdbdata().search_data
            print("success: search result of  {a} ".format(a=Imdbdata().search_data), " is coming")

        except NoSuchElementException as e:
            print(e)
