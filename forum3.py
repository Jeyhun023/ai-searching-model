from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
import time
from selenium.webdriver.chrome.options import Options
print("okey1")

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

print("options")

webdriver = webdriver.Chrome(executable_path="C:/Users/User/.wdm/drivers/chromedriver/win32/92.0.4515.107/chromedriver.exe")
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
#2
webdriver.execute_script("window.open('about:blank', '2');")
webdriver.switch_to.window("2")
webdriver.get(hrefs[1])
#3
webdriver.execute_script("window.open('about:blank', '3');")
webdriver.switch_to.window("3")
webdriver.get(hrefs[2])

sleep(2)

x = 1
timeout = time.time() + 340
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


*/6 * * * *  python3 /var/www/python/forum.py > /tmp/listener.log 2>&1


window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight)

var follow = document.getElementsByClassName("isgrP");
follow.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);

let array = [];
array = document.getElementsByClassName("sqdOP  L3NKy   y3zKF     ");
for (let i=0; i < 100; i++) {
    task(i);
}
    
function task(i) {
    setTimeout(function() {
        console.log(i);
        console.log(array.length);
        array[i].click();
    }, 17000 * i);
}  