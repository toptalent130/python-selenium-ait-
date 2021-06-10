from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import ait


API_KEY = "51f5efa7827b436fdd11172980d21623"
data_sitekey = '6LdaB7UUAAAAAD2w3lLYRQJqsoup5BsYXI2ZIpFF'
user_name = "kujacicmarko1001@gmail.com"
pass_word = "kujacicmarko10012010"


chrome_options = Options()
chrome_options.add_extension('E:\\Python\\scraping\\mining\\anticaptcha-plugin_v0.54.crx')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get('https://all-access.wax.io/')
print("----------------")

w1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[5]/div/div/div/div[1]/div[1]/input')
w1.send_keys(user_name)
print("---------------1")
w2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[5]/div/div/div/div[1]/div[2]/input')
w2.send_keys(pass_word)
print("---------------2")
# w3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[5]/div/div/div/div[4]/div/div/div/div/div/div/iframe')
# ait.move()
# ait.click()