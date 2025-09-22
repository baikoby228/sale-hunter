from asyncio import to_thread

import undetected_chromedriver as uc
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

async def get_html(article: int) -> str | None:
    return await to_thread(get_html_sync, article)

def get_html_sync(article: int) -> str | None:
    url = f'https://ozon.by/product/{article}'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    #user_agent = fake_useragent.UserAgent().random
    #chrome_options.add_argument(f'--user-agent={user_agent}')

    driver = uc.Chrome(options=chrome_options)
    #driver.maximize_window()
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.get(url)

    wait = WebDriverWait(driver, 10)

    for i in range(MAX_AMOUNT_OF_RETRIES):
        try:
            wait.until(EC.any_of(
                EC.presence_of_element_located((By.CLASS_NAME, "pdp_bb")),
                EC.presence_of_element_located((By.CLASS_NAME, "tsHeadline550Medium")),
                EC.presence_of_element_located((By.CLASS_NAME, "tsHeadline600Large"))
            ))
            break
        except TimeoutException:
            driver.refresh()

    if driver.find_elements(By.CLASS_NAME, "pdp_bb"):
        return None

    wait.until(EC.any_of(
        EC.presence_of_element_located((By.CLASS_NAME, "pdp_v5"))
    ))

    wait.until(EC.any_of(
        EC.presence_of_element_located((By.CLASS_NAME, "tsHeadline600Large"))
    ))

    html = driver.page_source
    driver.quit()

    return html

async def get_product(html: int) -> ProductData:
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