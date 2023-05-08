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


    bot.get('https://github.com/signup')


    time.sleep(5)

    bot.find_element(By.XPATH, '//*[@id="email"]').send_keys('peter_larry412@outlook.com')

    time.sleep(3)
    bot.find_element(By.XPATH, '//*[@id="email-container"]/div[2]/button').click()

    time.sleep(5)
    bot.find_element(By.XPATH, '//*[@id="password"]').send_keys('Nachiket@1998')
    
    time.sleep(3)
    bot.find_element(By.XPATH, '//*[@id="password-container"]/div[2]/button').click()

    time.sleep(5)
    bot.find_element(By.XPATH, '//*[@id="login"]').send_keys('peterlarry572')

    time.sleep(3)
    bot.find_element(By.XPATH, '//*[@id="username-container"]/div[2]/button').click()

    time.sleep(5)
    bot.find_element(By.XPATH, '//*[@id="opt_in"]').send_keys('n')

    time.sleep(3)
    bot.find_element(By.XPATH, '//*[@id="opt-in-container"]/div[2]/button').click()

    # time.sleep(5)
    # For Starting puzzle
    # bot.find_element(By.XPATH, '//*[@id="home_children_button"]').click()
    
    
    
  


    
    

    

    time.sleep(5)

    x = input('Done: y or n')

    if(x == 'y'):
        # bot.find_element(By.XPATH, '//*[@id="captcha-and-submit-container"]/button').click()
        #For Skip Persnalization button
        bot.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/div[3]/div/div/a').click()
        
        
        time.sleep(10)

        bot.get('https://github.com/jatinjd17')

        time.sleep(4)
        #For Clicking Follow button
        bot.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/span/form[1]/input[2]').click()

        time.sleep(4)
        #For CLicking Repository stars

        bot.get('https://github.com/jatinjd17?tab=repositories')

        time.sleep(4)

        for i in range(25):
            num = i + 1
            bot.find_element(By.XPATH, f'//*[@id="user-repositories-list"]/ul/li[{num}]/div[2]/div[1]/div[2]/form/button').click()
            actions = ActionChains(bot) 


            actions.send_keys(Keys.DOWN)
            time.sleep(0.5)
            actions.send_keys(Keys.DOWN)

        
        

        print("Done!!!!!!")
        time.sleep(5000)
    bot.quit()


if __name__ == "__main__":
    RunScript()
