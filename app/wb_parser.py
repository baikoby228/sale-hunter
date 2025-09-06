from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import fake_useragent

def parse_bs(html) -> str:
    soup = BeautifulSoup(html, "lxml")
    res = soup.find("ins", class_='priceBlockFinalPrice--iToZR').text
    return res

def parse_selenium(article):
    url = f'https://www.wildberries.by/catalog/{article}/detail.aspx'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    user_agent = fake_useragent.UserAgent().random
    chrome_options.add_argument(f'--user-agent={user_agent}')

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.get(url)

    wait = WebDriverWait(driver, 10000)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "priceBlockFinalPrice--iToZR")))

    return driver.page_source

def wb_parser(article) -> str:
    html = parse_selenium(article)
    return parse_bs(html)

if __name__ == "__main__":
    article = int(input('Введите артикул:\n'))
    print(f'Цена - {wb_parser(article)}')
