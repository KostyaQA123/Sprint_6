import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self, index):
        return self.driver.window_handles[index]

    @allure.step('Переключить вкладку')
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not found {locator}')

    def find_visible_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator), message=f'Not found {locator}')

    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not found {locator}')

    @allure.step('Ожидание URL {url}')
    def wait_for_url(self, url, time=90):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url), message=f'Page URL is not {url} after {time} sec')
