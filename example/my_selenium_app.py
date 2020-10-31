""" Selenium example

Just reading the content of https://python.org

"""
from selenium.webdriver.chrome.webdriver import WebDriver


def main(driver: WebDriver):
    driver.get('https://python.org')
    print(driver.page_source)
