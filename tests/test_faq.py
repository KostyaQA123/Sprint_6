import pytest
import allure

from pages.home_page import HomePage
from utils.expected_answers import FAQAnswers


@allure.epic('Test FAQ')
class TestFAQ:
    @allure.feature('FAQ')
    @allure.title('FAQ')
    @allure.story('FAQ Interaction')
    @pytest.mark.parametrize(
        'question_n, answer_n, answer_text',
        [
            (0, 0, FAQAnswers.answer_1),
            (1, 1, FAQAnswers.answer_2),
            (2, 2, FAQAnswers.answer_3),
            (3, 3, FAQAnswers.answer_4),
            (4, 4, FAQAnswers.answer_5),
            (5, 5, FAQAnswers.answer_6),
            (6, 6, FAQAnswers.answer_7),
            (7, 7, FAQAnswers.answer_8)
        ]
    )
    def test_click_on_faq_questions(self, driver, question_n, answer_n, answer_text):
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        home_page.confirm_cookies()
        home_page.scroll_to_faq()
        home_page.click_on_question(question_n)
        answer = home_page.get_answer(answer_n)
        assert answer.is_displayed() and answer.text == answer_text
