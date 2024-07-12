from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class HomePageLocators:
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']/parent::a")
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']/parent::a")
    CONFIRM_COOKIES_BUTTON = (By.ID, 'rcc-confirm-button')
    FAQ_HEADER = (By.XPATH, ".//div[text()='Вопросы о важном']")
    QUESTIONS = (By.XPATH, ".//div[contains(@id, 'accordion__heading')]")
    ANSWERS = (By.XPATH, ".//div[contains(@id, 'accordion__panel')]/p")
    TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")


class HomePage(BasePage):
    @allure.step('Принять куки')
    def confirm_cookies(self):
        return self.find_element_located(HomePageLocators.CONFIRM_COOKIES_BUTTON).click()

    @allure.step('Скролить страницу до раздела FAQ')
    def scroll_to_faq(self):
        faq_header = self.find_element_located(HomePageLocators.FAQ_HEADER)
        return self.driver.execute_script("arguments[0].scrollIntoView();", faq_header)

    def scroll_to_bottom_order_button(self):
        order_button = self.find_element_located(HomePageLocators.BOTTOM_ORDER_BUTTON)
        return self.driver.execute_script("arguments[0].scrollIntoView();", order_button)

    @allure.step('Кликнуть на вопрос')
    def click_on_question(self, index):
        questions = self.find_visible_elements_located(HomePageLocators.QUESTIONS)
        return questions[index].click()

    def get_answer(self, index):
        answers = self.find_elements_located(HomePageLocators.ANSWERS)
        return answers[index]

    @allure.step('Кликнуть на кнопку Заказать')
    def click_make_order(self, is_bottom=False):
        if is_bottom:
            self.scroll_to_bottom_order_button()
            return self.find_clickable_element(HomePageLocators.BOTTOM_ORDER_BUTTON).click()
        return self.find_clickable_element(HomePageLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Кликнуть на лого скутера')
    def click_scooter_logo(self):
        return self.find_clickable_element(HomePageLocators.SCOOTER_LOGO).click()

    @allure.step('Кликнуть на лого Яндекса')
    def click_yandex_logo(self):
        return self.find_clickable_element(HomePageLocators.YANDEX_LOGO).click()
