from time import sleep

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from tests.test_login import firefox_webdriver


def test_single_page_navigation():
    with firefox_webdriver() as driver:
        driver.get('http://localhost:8080/spa')
        sleep(3)
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout=2, ignored_exceptions=errors)

        content_one_label: WebElement = driver.find_element(By.ID, 'page-one-label')
        wait.until(lambda d: content_one_label.is_displayed())
        assert content_one_label.text == 'Content One'
        assert driver.current_url == 'http://localhost:8080/spa/'

        page_one_button = driver.find_element(By.ID, 'page-one-button')
        page_two_button = driver.find_element(By.ID, 'page-two-button')
        page_three_button = driver.find_element(By.ID, 'page-three-button')

        page_two_button.click()
        content_two_label: WebElement = driver.find_element(By.ID, 'page-two-label')
        wait.until(lambda d: content_two_label.is_displayed())
        assert content_two_label.text == 'Content Two'
        assert driver.current_url == 'http://localhost:8080/spa/two'

        page_three_button.click()
        content_three_label: WebElement = driver.find_element(By.ID, 'page-three-label')
        wait.until(lambda d: content_three_label.is_displayed())
        assert content_three_label.text == 'Content Three'
        assert driver.current_url == 'http://localhost:8080/spa/three'

        page_one_button.click()
        content_one_label: WebElement = driver.find_element(By.ID, 'page-one-label')
        wait.until(lambda d: content_one_label.is_displayed())
        assert content_one_label.text == 'Content One'
        assert driver.current_url == 'http://localhost:8080/spa/'
