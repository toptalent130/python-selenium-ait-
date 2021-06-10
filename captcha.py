from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import requests, time
import pickle

API_KEY = "51f5efa7827b436fdd11172980d21623"
# API_KEY = "9c3aee1efcd34573aecee06b82aef440"
data_sitekey = '6LdaB7UUAAAAAD2w3lLYRQJqsoup5BsYXI2ZIpFF'
page_url ='https://all-access.wax.io/'

def Solver():
    # driver = webdriver.Chrome(executable_path='D:\data 3\Selenium\Web\chromedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.maximize_window()
    driver.get(page_url)
    time.sleep(5)
    u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
    r1 = requests.get(u1)
    time.sleep(5)
    rid = r1.json().get("request")
    time.sleep(5)
    u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
    time.sleep(5)
    form_token = ''
    while True:
        r2 = requests.get(u2)
        print(r2.json())
        time.sleep(5)
        if r2.json().get("status") == 1:
            form_token = r2.json().get("request")
            time.sleep(20)
            driver.execute_script(f"document.getElementById('g-recaptcha-response-1').innerHTML='{form_token}'")
            time.sleep(7)
            driver.execute_script(f"___grecaptcha_cfg.clients[0].B.B.callback('{form_token}')")
            time.sleep(30)
            break
    username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[5]/div/div/div/div[1]/div[1]/input').send_keys('chrlschwb@gmail.com')
    time.sleep(3)
    password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[5]/div/div/div/div[1]/div[2]/input').send_keys('op[]OP{}90-=()_+')
    time.sleep(3)
    login = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[5]/div/div/div/div[5]/button[1]').click()
    time.sleep(300)
    # driver.execute_script("document.getElementById('g-recaptcha-response-1').style.display='block'")
    # time.sleep(7)
    # driver.execute_script("document.getElementsByClassName('button-secondary')[2].disabled = false")
    # time.sleep(15)
    # login = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div/div/div[5]/button[1]').click()
    # time.sleep(3)
    # username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div/div/div[1]/div[1]/input').send_keys('chrlschwb@gmail.com')
    # time.sleep(3)
    # password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div/div/div[1]/div[2]/input').send_keys('op[]OP{}90-=()_+')
    # time.sleep(3)
    # driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='{}';".format(form_token))
    # time.sleep(10)
    # driver.execute_script("document.getElementByClassName('button-secondary')[2].setAttribute('disabled', false)")
    # time.sleep(3)
    # driver.execute_script("document.getElementById('g-recaptcha-response').style.display='block'")
    # login = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div/div/div[5]/button[1]').click()
    # time.sleep(3)
    # /html/body/div[1]/div/div/div[2]/div[5]/div/div/div/div[5]/button[1]
#     time.sleep(10)

if __name__ == '__main__':
    Solver()
