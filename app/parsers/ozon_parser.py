import asyncio
from asyncio import to_thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import fake_useragent

from config import INF, MAX_AMOUNT_OF_RETRIES
from utils import find_number
from models import ProductData

import os
from datetime import datetime
def save_debug_screenshot(driver, prefix="retry_fail"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{prefix}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    path = os.path.join("screenshots", filename)
    driver.save_screenshot(path)
    print(f'path - {path}')

async def get_html(article) -> str | None:
    return await to_thread(_get_html_sync, article)

import time
def _get_html_sync(article) -> str | None:
    url = f'https://ozon.by/product/{article}'

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    user_agent = fake_useragent.UserAgent().random
    chrome_options.add_argument(f'--user-agent={user_agent}')

    driver = webdriver.Chrome(options=chrome_options)
    #driver.maximize_window()
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.get(url)

    wait = WebDriverWait(driver, 10)

    asyncio.sleep(3.9713)
    '''
    time.sleep(30)
    with open("code.txt", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    '''

    success = False
    for i in range(MAX_AMOUNT_OF_RETRIES):
        try:
            wait.until(EC.any_of(
                EC.presence_of_element_located((By.CLASS_NAME, "pdp_bb")),
                EC.presence_of_element_located((By.CLASS_NAME, "tsHeadline550Medium")),
                EC.presence_of_element_located((By.CLASS_NAME, "tsHeadline600Large"))
            ))
            success = True
            break
        except TimeoutException:
            driver.refresh()

    if driver.find_elements(By.CLASS_NAME, "pdp_bb"):
        return None

    if not success:
        save_debug_screenshot(driver, prefix="element_not_found")
        raise TimeoutException("Не нашёл")

    #pdp_v5 pdp_v6 b95_3_1-a
    wait.until(EC.any_of(
        EC.presence_of_element_located((By.CLASS_NAME, "pdp_v6"))
    ))

    wait.until(EC.any_of(
        EC.presence_of_element_located((By.CLASS_NAME, "tsHeadline600Large"))
    ))

    return driver.page_source

async def get_product(html) -> ProductData:
    res = ProductData()

    soup = BeautifulSoup(html, "lxml")

    res.name = soup.find("h1", class_='pdp_bf7 tsHeadline550Medium').text.strip()

    price_block = soup.find("span", class_='pdp_bf2 tsHeadline600Large')
    if not price_block:
        res.current_price = INF
    else:
        res.current_price = find_number(price_block.text)

    res.photo_url = soup.find("img", class_='pdp_v5 pdp_v6 b95_3_1-a')['src']

    return res

async def ozon_parser(article: int) -> ProductData | None:
    html = await get_html(article)
    if not html:
        return None
    return await get_product(html)

if __name__ == "__main__":
    article = 2415425494
    html = get_html(article)
    with open('code.txt', 'a', encoding='utf-8') as f:
        print(html, file=f)