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


    bot.get('https://en-gb.facebook.com/')

    time.sleep(5)
    

    #For Allow Cookies Button
    # bot.find_element(By.XPATH, '//*[@id="u_0_k_tf"]').click()
    bot.find_element(By.CSS_SELECTOR, 'button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy').click()

    time.sleep(3)


    #For Creat New Account Button

    # bot.find_element(By.XPATH, '//*[@id="u_0_0_Xt"]').click()
    bot.find_element(By.CSS_SELECTOR, 'a._42ft._4jy0._6lti._4jy6._4jy2.selected._51sy').click()
    
    
    


    time.sleep(5)
    #for Email
    # bot.find_element(By.XPATH, '//*[@id="u_5_g_Rr"]').send_keys('mark_hubbard45517@outlook.com')
    bot.find_element(By.CSS_SELECTOR, 'input.inputtext._58mg._5dba._2ph-').send_keys('mark_hubbard45517@outlook.com')
    
    time.sleep(2)
    # bot.find_element(By.XPATH, '//*[@id="u_5_j_G9"]').send_keys('mark_hubbard45517@outlook.com')
    bot.find_element(By.CSS_SELECTOR, 'input.inputtext._58mg._5dba._2ph-').send_keys('mark_hubbard45517@outlook.com')
    
    time.sleep(0.5)
    #For Name
    # bot.find_element(By.XPATH, '//*[@id="u_5_b_BM"]').send_keys('mark')
    bot.find_element(By.CSS_SELECTOR, 'input.inputtext._58mg._5dba._2ph-').send_keys('mark')
    
    time.sleep(0.5)
    #For LastName
    # bot.find_element(By.XPATH, '//*[@id="u_5_d_48"]').send_keys('hubbard')
    bot.find_element(By.XPATH, 'input.inputtext._58mg._5dba._2ph-').send_keys('hubbard')
    
    time.sleep(0.5)
    #For Password
    # bot.find_element(By.XPATH, '//*[@id="password_step_input"]').send_keys('Jatin@123')
    bot.find_element(By.XPATH, 'input.inputtext._58mg._5dba._2ph-').send_keys('Jatin@123')
    
    time.sleep(0.5)
    #For Date
    bot.find_element(By.XPATH, '//*[@id="day"]/option[13]').click()
    time.sleep(0.5)
    #For Month
    bot.find_element(By.XPATH, '//*[@id="month"]/option[6]').click()
    time.sleep(0.5)
    #For Year
    bot.find_element(By.XPATH, '//*[@id="year"]/option[29]').click()
    time.sleep(0.5)

    #For Gender
    # bot.find_element(By.XPATH, '//*[@id="u_5_5_Yb"]').click()
    bot.find_element(By.CSS_SELECTOR, 'input._8esa').click()
    
    time.sleep(2)
    #For SignUP Button
    # bot.find_element(By.XPATH, '//*[@id="u_5_s_h4"]').click()
    bot.find_element(By.XPATH, 'button._6j.mvm._6wk._6wl._58mi._3ma._6o._6v').click()
    
    
    time.sleep(10)

    x = input('Done FaceBook Signup?: y or n')

    if(x == 'y'):
        # bot.find_element(By.XPATH, '//*[@id="captcha-and-submit-container"]/button').click()
        #For Skip Persnalization button
        bot.get('https://www.facebook.com/')
        
        
        

        
        

        print("Done!!!!!!")
        time.sleep(50000)
    bot.quit()


if __name__ == "__main__":
    RunScript()
