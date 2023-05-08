import time, os
import random
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
# options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')
# options.add_argument(f'user-agent=Chrome/113.0.0.0')
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
# # options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--log-level=3")
# options.add_argument(r"--user-data-dir=C:\Users\jatin\AppData\Local\Google\Chrome\User Data") 
# options.add_argument(r"--user-data-dir=C:\Users\student_00_fc1ec9f2e\AppData\Local\Google\Chrome\User Data") 
	
#e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# options.add_argument('profile-directory=Default')
# options.add_argument('--window-size=1920,1080')
#options.add_argument("--headless")
time.sleep(2)

def RunScript():
    bot = webdriver.Chrome(chrome_options=options)

    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    firstname = (names.get_first_name(gender='male')).lower()
    lastname = (names.get_last_name()).lower()
    email = firstname+'_'+lastname+str(random.randrange(7598,100000))+'@outlook.com'
    print(email)

    # print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')

    try:

        bot.get('https://www.google.com/')
        time.sleep(3)
        bot.get('https://signup.live.com/signup')
       
        # time.sleep(4)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="MemberName"]'))).send_keys(email)

        # bot.find_element(By.XPATH, '//*[@id="MemberName"]').send_keys(email)


        # time.sleep(1)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()


        # time.sleep(5)
        
        #For Password Imput
        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PasswordInput"]'))).send_keys('Jatin@123')

        # bot.find_element(By.XPATH, '//*[@id="PasswordInput"]').send_keys('Jatin@123')

        

        # time.sleep(1)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

        

        # time.sleep(4)
        
        #For Name And Lastname
        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FirstName"]'))).send_keys(firstname)

        # bot.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys(firstname)
    

        # time.sleep(1)
        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="LastName"]'))).send_keys(lastname)


        # bot.find_element(By.XPATH, '//*[@id="LastName"]').send_keys(lastname)
       

        # time.sleep(1)
        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

        # time.sleep(4)
        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BirthMonth"]/option[6]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="BirthMonth"]/option[6]').click()
        # time.sleep(1)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BirthDay"]/option[10]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="BirthDay"]/option[10]').click()
        # time.sleep(1)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BirthYear"]'))).send_keys('1993')

        # bot.find_element(By.XPATH, '//*[@id="BirthYear"]').send_keys('1993')
        # time.sleep(1)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

        #OutlookDone? Then ->
        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idBtn_Back"]'))).click()

        
        time.sleep(5)

        bot.get('https://outlook.live.com/mail/0/')

        print("Outlook Done!!!!!!")

        bot.execute_script("window.open('');")

        time.sleep(2)

        bot.switch_to.window(bot.window_handles[1])

        bot.get('https://github.com/signup')


        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))).send_keys(email)

        time.sleep(2)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-container"]/div[2]/button'))).click()

        time.sleep(2)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('Nachiket@1998')

        time.sleep(2)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password-container"]/div[2]/button'))).click()

        githubusername = firstname+lastname+str(random.randrange(10598,100000))

        time.sleep(2)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]'))).send_keys(githubusername)

        time.sleep(2)
      
        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username-container"]/div[2]/button'))).click()

        time.sleep(2)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="opt_in"]'))).send_keys('n')

        time.sleep(2)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="opt-in-container"]/div[2]/button'))).click()

        time.sleep(3)


        # WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="captcha-and-submit-container"]/button'))).click()



        
        

        # Github Done? -> Then

        bot.switch_to.window(bot.window_handles[0])
        
        elee2 = WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue signing up for GitHub by entering the code below')]")))
                
        ttext2 = elee2.text


        githubcode = ttext2.split("below: ")[1].split(" Open")[0]

        print(githubcode)

        bot.switch_to.window(bot.window_handles[1])

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="launch_code[]"]'))).send_keys(githubcode)


        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/div[3]/div/div/a'))).click()

        time.sleep(10)

        bot.get('https://github.com/jatinjd17')

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/span/form[1]/input[2]'))).click()

        time.sleep(4)
        
        #For CLicking Repository stars

        bot.get('https://github.com/jatinjd17?tab=repositories')

        time.sleep(4)

        for i in range(29):
            num = i + 1
            WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH,  f'//*[@id="user-repositories-list"]/ul/li[{num}]/div[2]/div[1]/div[2]/form/button'))).click()
            actions = ActionChains(bot) 
            actions.send_keys(Keys.DOWN)
            time.sleep(0.2)
            actions.send_keys(Keys.DOWN)
        print("Done Github!!!!!!")

        bot.execute_script("window.open('');")
        time.sleep(2)

        bot.switch_to.window(bot.window_handles[2])
        time.sleep(2)

        bot.get('https://en-gb.facebook.com/')

        time.sleep(10)


        try:


            bot.find_element(By.CSS_SELECTOR, 'button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy').click()
        except:
            pass
        # WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy'))).click()


        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a._42ft._4jy0._6lti._4jy6._4jy2.selected._51sy'))).click()

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_email__"]'))).send_keys(email)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_email_confirmation__"]'))).send_keys(email)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="firstname"]'))).send_keys(firstname)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="lastname"]'))).send_keys(lastname)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_passwd__"]'))).send_keys('Jatin@123')


        randdate = random.randint(3,20)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="day"]/option[{randdate}]'))).click()


        randmonth = random.randint(2,9)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="month"]/option[{randmonth}]'))).click()

        randyear = random.randint(28, 34)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="year"]/option[{randyear}]'))).click()

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[value="2"]'))).click()

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="websubmit"]'))).click()


        time.sleep(25)

        #Going Outlook For OTP Code
        bot.switch_to.window(bot.window_handles[0])


        elee = WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'is your Facebook confirmation code')]")))

        ttext = elee.text

        facebookcode = ttext.replace('FB-',"").replace(" is your Facebook confirmation code","")
        
        print(facebookcode)

        time.sleep(1)

        bot.switch_to.window(bot.window_handles[2])

        time.sleep(2)

        ###############NOTEE##########
        #Put This code using send_keys

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="code_in_cliff"]'))).send_keys(facebookcode)

        WebDriverWait(bot,2000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="confirm"]'))).click()
                
        time.sleep(20)
        # Then Click Next
        bot.get('https://www.facebook.com/')

        print("Done Facebook!!!!!!")

        bot.execute_script("window.open('');")
        time.sleep(2)

        bot.switch_to.window(bot.window_handles[3])
        time.sleep(2)



        bot.get('https://www.instagram.com/')


         
        time.sleep(50000)
        bot.quit()
    except Exception as e:
        print(e)
        time.sleep(10000)



if __name__ == "__main__":
    RunScript()
