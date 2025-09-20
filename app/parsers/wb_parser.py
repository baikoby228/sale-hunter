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

async def get_html(article: int) -> str | None:
    return await to_thread(get_html_sync, article)

def get_html_sync(article: int) -> str | None:
    url = f'https://www.wildberries.by/catalog/{article}/detail.aspx'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
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

    '''
    time.sleep(30)
    with open("code.txt", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    '''

    for i in range(MAX_AMOUNT_OF_RETRIES):
        try:
            wait.until(EC.any_of(
                EC.presence_of_element_located((By.CLASS_NAME, "content404")),
                EC.presence_of_element_located((By.CLASS_NAME, "productTitle--J2W7I")),
                EC.presence_of_element_located((By.CLASS_NAME, "soldOutProductText--hhsT1"))
            ))
            break
        except TimeoutException:
            driver.refresh()

    if driver.find_elements(By.CLASS_NAME, "content404"):
        return None

    wait.until(EC.any_of(
        EC.presence_of_element_located((By.CLASS_NAME, "verticalSlide--fBKUm")),
        EC.presence_of_element_located((By.CLASS_NAME, "miniatureSlide--acvJc"))
    ))

    wait.until(EC.any_of(
        EC.presence_of_element_located((By.CLASS_NAME, "priceBlockFinalPrice--iToZR")),
        EC.presence_of_element_located((By.CLASS_NAME, "soldOutProductText--hhsT1"))
    ))

    return driver.page_source

async def get_product(html) -> ProductData:
    res = ProductData()

    soup = BeautifulSoup(html, "lxml")

    res.name = soup.find("h1", class_='productTitle--J2W7I').text

    price_block = soup.find("ins", class_='priceBlockFinalPrice--iToZR')
    if not price_block:
        res.current_price = INF
    else:
        res.current_price = find_number(price_block.text)

    flag = True
    wrapper = soup.find("div", class_='swiper-wrapper verticalWrapper--K5LVG')
    if wrapper:
        divs = wrapper.find_all("div", class_=['swiper-slide', 'verticalSlide--fBKUm'])
        if not divs:
            flag = False
    else:
        flag = False

    if not flag:
        divs = soup.find("div", class_='swiper-wrapper miniaturesWrapper--PF0rM').find_all("div", class_=['swiper-slide', 'miniatureSlide--acvJc'])

    for div in divs:
        photo = div.find('img')
        if photo:
            res.photo_url = photo['src']
            break

    return res

async def wb_parser(article: int) -> ProductData | None:
    html = await get_html(article)
    if not html:
        return None
    return await get_product(html)

'''
if __name__ == "__main__":
    article = int(input('Введите артикул:\n'))
    print(f'Цена - {wb_parser(article).current_price}')
'''