from ET_pages_aqa.base_page import Page
from ET_pages_aqa.header import Header
from ET_pages_aqa.main_page import MainPage
from ET_pages_aqa.search_results_page import SearchResultsPage
from ET_pages_aqa.cart_page import CartPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)


