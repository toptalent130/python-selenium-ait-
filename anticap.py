from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import ait
# import ait
API_KEY = "65a13c871b9992dc2e2d78ccbfd5bbe4"
data_sitekey = '6LdaB7UUAAAAAD2w3lLYRQJqsoup5BsYXI2ZIpFF'
page_url ='https://all-access.wax.io/'
user_name = 'chrlschwb@gmail.com'
pass_word = 'op[]OP{}90-=()_+'
def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_extension('E:\\Python\\scraping\\mining\\anticaptcha-plugin_v0.54.crx')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.set_window_position(0,0)
    # driver.set_window_size(480, 320)
    driver.get('https://all-access.wax.io/')
    time.sleep(20)
    ait.move(820,57)
    ait.click()
    time.sleep(10)
    ait.move(344,221)
    ait.click()
    time.sleep(1)
    ait.write(API_KEY)
    time.sleep(100)
if __name__ == '__main__':
    main()