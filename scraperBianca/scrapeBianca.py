from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import boto3
import json


def scrape_bianca_home():
    options = Options()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.bianca.com")
    html_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')
    products = soup.find_all('div', class_='product')
    data = []

    for product in products:
        title = product.find('h2', class_='product-title').text
        price = product.find('span', class_='product-price').text
        data.append({'title': title, 'price': price})

    s3 = boto3.client('s3')
    bucket_name = 'diogoaws'
    file_name = 'products.json'

    s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))

    return data
