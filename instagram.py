from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#Select the driver, In our case we will use Chrome.
webdriver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_extension('Adblock-Plus_v1.4.1.crx')
options.add_argument('--user-data-dir=C:\Users\username\ChromeProfiles\User Data')
webdriver = webdriver.Chrome(chrome_options=options)

sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)
username = webdriver.find_element_by_name('username')
username.send_keys('merve.pin4r')
password = webdriver.find_element_by_name('password')
password.send_keys('888akif2001')
#instead of searching for the Button (Log In) you can simply press enter when you already selected the password or the username input element.
submit = webdriver.find_element_by_tag_name('form')
submit.submit()
sleep(4)

webdriver.get('https://www.instagram.com/mizahkar1adam')
sleep(4)

webdriver.find_element_by_class_name('eLAPa').click()
sleep(3)

el = webdriver.find_element_by_class_name('zV_Nj').click()
sleep(3)

i = 0

while True:

    users = webdriver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div')

    users = users.find_elements_by_tag_name('button')

    for user in users: 
        text = user.get_attribute('innerHTML')
        if text == "Follow":
            user.click()
            sleep(15)
            i = i + 1
        if i % 5 == 0:
            sleep(60)
 
    webdriver.find_element_by_class_name('_1XyCr').click()
    
    ActionChains(webdriver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    sleep(3)
    ActionChains(webdriver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    sleep(3)
    ActionChains(webdriver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    sleep(3)
    ActionChains(webdriver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    sleep(3)



