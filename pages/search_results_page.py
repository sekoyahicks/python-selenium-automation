from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")

    def verify_text(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
        assert 'toothpaste' in actual_text, f'Expected toothpaste not in actual {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'toothpaste' in url, f'Expected "toothpaste" not in {url}'
