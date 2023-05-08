import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# options.add_argument('--window-size=1920,1080')
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")


# Exclude the collection of enable-automation switches
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Turn-off userAutomationExtension
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')
# # options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--log-level=3")
# options.add_argument(r"--user-data-dir=C:\Users\jatin\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# options.add_argument('profile-directory=Default')
# options.add_argument('--window-size=1920,1080')
#options.add_argument("--headless")
time.sleep(2)

def RunScript():
    bot = webdriver.Chrome(chrome_options=options)

    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


    bot.get('https://www.google.com/')
    time.sleep(3)
    bot.get('https://signup.live.com/signup')
    # ?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1683292043&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3db1f90bed-dbf0-351e-1816-aeb35d718d24&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=1b306e0846814a9894510ff19eaebbe8
    time.sleep(4)

    bot.find_element(By.XPATH, '//*[@id="MemberName"]').send_keys('jake_henson983@outlook.com')

    # bot.find_element_by_xpath('//*[@id="MemberName"]').send_keys('peter_larry412')

    time.sleep(2)

    bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    # bot.find_element_by_xpath('//*[@id="iSignupAction"]').click()

    time.sleep(5)
    
    #For Password Imput

    bot.find_element(By.XPATH, '//*[@id="PasswordInput"]').send_keys('Jatin@123')

    # bot.find_element_by_xpath('//*[@id="PasswordInput"]').send_keys('Jatin@123')

    time.sleep(2)

    bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    # bot.find_element_by_xpath('//*[@id="iSignupAction"]').click()

    time.sleep(4)
    
    #For Name And Lastname
    bot.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys('jake')
    # bot.find_element_by_xpath('//*[@id="FirstName"]').send_keys('peter')

    time.sleep(2)
    bot.find_element(By.XPATH, '//*[@id="LastName"]').send_keys('henson')
    # bot.find_element_by_xpath('//*[@id="LastName"]').send_keys('larry')

    time.sleep(2)
    bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    time.sleep(4)
    bot.find_element(By.XPATH, '//*[@id="BirthMonth"]/option[6]').click()
    time.sleep(2)
    bot.find_element(By.XPATH, '//*[@id="BirthDay"]/option[10]').click()
    time.sleep(2)
    bot.find_element(By.XPATH, '//*[@id="BirthYear"]').send_keys('1993')
    time.sleep(2)
    bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()
  


    
    

    

    time.sleep(5)

    x = input('Done: y or n')

    if(x == 'y'):
        time.sleep(4)
        bot.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()

        time.sleep(5)
        

        print("Done!!!!!!")
        time.sleep(50000)
    bot.quit()


if __name__ == "__main__":
    RunScript()
