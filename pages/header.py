from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search(self):
        self.input_text('toothpaste', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

        sleep(6)
