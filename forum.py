from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
from selenium.webdriver.chrome.options import Options
import time
print("okey")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

print("options")

webdriver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options=chrome_options)
sleep(2)

print("setoptions")

webdriver.get('https://community.goodgamestudios.com/empire/tr/discussions?save=1&TransientKey=HzLOtOtXM4N7AxVS&followed=0')

print("getting")

sleep(3)
hrefs = []

aTagsInLi = webdriver.find_elements_by_css_selector('li a')
for a in aTagsInLi:
    href = a.get_attribute('href')
    if href.find("discussion/") != -1:
        hrefs.append(href)

random.shuffle(hrefs)

#1
webdriver.execute_script("window.open('about:blank', '1');")
webdriver.switch_to.window("1")
webdriver.get(hrefs[0])
print(hrefs[0])
#2
webdriver.execute_script("window.open('about:blank', '2');")
webdriver.switch_to.window("2")
webdriver.get(hrefs[1])
print(hrefs[1])
#3
webdriver.execute_script("window.open('about:blank', '3');")
webdriver.switch_to.window("3")
webdriver.get(hrefs[2])
print(hrefs[2])

sleep(2)

x = 1
timeout = time.time() + 345
while time.time() < timeout:
    print("try {}".format(x))
    webdriver.switch_to.window("1")
    webdriver.refresh()
    webdriver.switch_to.window("2")
    webdriver.refresh()
    webdriver.switch_to.window("3")
    webdriver.refresh()
    sleep(1)
    x = x + 1

webdriver.quit()

*/6 * * * *  python3 /var/www/api_abysshub/php artisan search:reindex > /tmp/listener.log 2>&1
* * * * */5  python3 /var/local/python/productBot.py > /tmp/listener.log 2>&1
* * * * */5  python3 /var/local/python/stackoverflow.py > /tmp/listener.log 2>&1

*/6 * * * * /var/www/api_abysshub/php artisan search:reindex >/dev/null 2>&1