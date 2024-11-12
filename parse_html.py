import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_html():

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(options=op)
    url = 'https://rostics.ru/promo/crazydays'
    driver.get(url)
    time.sleep(5)
    page_text = driver.find_element(By.CLASS_NAME, 'hWtfcfE9CFC')
    time.sleep(1)
    text_h1 = page_text.find_element(By.CSS_SELECTOR, 'h1')
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR, "div[style*='background-image']")
    style = element.get_attribute("style")
    url = re.search(r'url\("(.+?)"\)', style).group(1)

    return text_h1.text, url




