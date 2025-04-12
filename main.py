from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests


SITE_URL = 'https://appbrewery.github.io/Zillow-Clone/'
DOC_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSeHAY2u7Fn-EuGuPJtdyoPaDFWMeZ-a2_8_NHEVnw_7uSOBkg/viewform?usp=dialog'


# beautifulsoup
# Open the site with requests
response = requests.get(SITE_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# pega os endereços, preços e links dos imóveis
adresses = soup.find_all('address')
adresses = [addr.text.strip() for addr in adresses]

prices = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
prices = [float(price.text.strip('$+ 1 bdmo/').replace(',','.')) for price in prices]

property_links = soup.find_all('a', class_='property-card-link')
property_links = [link['href'] for link in property_links]



op = webdriver.ChromeOptions()
op.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=op)
driver.get(DOC_URL)  # abre o site
driver.maximize_window()
time.sleep(1)



for i in range(len(adresses)):
    adrr_box = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_box = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    
    adrr_box.send_keys(adresses[i])
    price_box.send_keys(prices[i])
    link_box.send_keys(property_links[i])
    send_box.click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(2)