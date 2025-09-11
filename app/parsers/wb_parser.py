from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import fake_useragent

from utils import find_number
from ..session import ProductData

def get_html(article) -> str | None:
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

    wait = WebDriverWait(driver, 30)

    '''
    time.sleep(30)
    with open("code.txt", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    '''

    wait.until(EC.any_of(
        EC.presence_of_element_located((By.CLASS_NAME, "content404")),
        EC.presence_of_element_located((By.CLASS_NAME, "productTitle--J2W7I"))
    ))

    if driver.find_elements(By.CLASS_NAME, "content404"):
        return None

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "verticalSlide--fBKUm")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "priceBlockFinalPrice--iToZR")))

    return driver.page_source

def get_product(html) -> ProductData:
    res = ProductData()

    soup = BeautifulSoup(html, "lxml")

    res.name = soup.find("h1", class_='productTitle--J2W7I').text
    res.current_price = find_number(soup.find("ins", class_='priceBlockFinalPrice--iToZR').text)

    divs = soup.find("div", class_='swiper-wrapper verticalWrapper--K5LVG').find_all("div", class_=['swiper-slide', 'verticalSlide--fBKUm'])
    for div in divs:
        photo = div.find('img')
        if photo:
            res.photo_url = photo['src']
            break

    return res

def wb_parser(article: int) -> ProductData | None:
    html = get_html(article)
    if not html:
        return None
    return get_product(html)

'''
if __name__ == "__main__":
    article = int(input('Введите артикул:\n'))
    print(f'Цена - {wb_parser(article).current_price}')
'''