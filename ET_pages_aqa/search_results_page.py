from ET_pages_aqa.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results_correct(self, expected_results):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert expected_results == actual_text, f'Expected word {expected_results} not in {actual_text}'

    def verify_search_results_page_url(self, expected_part_url):
        url = self.driver.current_url
        assert expected_part_url in url, f'Expected {expected_part_url} not in {url}'
