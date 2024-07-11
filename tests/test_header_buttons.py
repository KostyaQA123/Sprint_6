import pytest
import allure

from pages.home_page import HomePage


@allure.epic('Test Header Link Buttons')
class TestHeaderLinkButtons:
    @allure.feature('Переход на главную страницу')
    @allure.title('Переход на главную страницу')
    def test_go_to_homepage_button(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        home_page.confirm_cookies()
        home_page.click_make_order()
        home_page.click_scooter_logo()
        home_page.wait_for_url("https://qa-scooter.praktikum-services.ru/")
        assert home_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

    @allure.feature('Переход на страницу Яндекса')
    @allure.title('Переход на страницу Яндекса')
    def test_go_to_yandex_homepage_button(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        home_page.confirm_cookies()
        home_page.click_yandex_logo()
        yandex_tab = home_page.get_window_handles(1)
        home_page.switch_to_window(yandex_tab)
        home_page.wait_for_url("https://dzen.ru/?yredirect=true")
        assert home_page.get_current_url() == "https://dzen.ru/?yredirect=true"
