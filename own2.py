from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests, json

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
print('loading')
# service=Service("/usr/lib/chromium-browser/chromedriver")
webdriver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options=chrome_options)
sleep(2)
print('starting')

def get_access_token():
    url = 'https://api.abysshub.com/api/login' # Set destination URL here
    data = {'email': 'creshidov23@gmail.com', 'password': '888ceyhun'}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":"text/plain"}
    response = requests.post(url, data=data, headers=headers)

    response_dict = json.loads(response.text)
    access_token = response_dict['data']['access_token']
    print('getting access token')
    return access_token

def submit_answer(headers, thread_id, answer):
    url = f'https://api.abysshub.com/api/forum/{thread_id}/answer/submit' # Set destination URL here
    data = {'content' : answer.get_attribute('innerHTML')}
    requests.post(url, data=data, headers=headers)
    print('submitting answer')
    sleep(1)

def submit_thread(access_token, title, body, tags):
    url = 'https://api.abysshub.com/api/forum/create' # Set destination URL here
    data = {'category_id': 1, 'title': title, 'content' : body, 'tags' : tags}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":"text/plain", "Authorization": "Bearer " + access_token}
    response = requests.post(url, data=data, headers=headers)
            
    response_dict = json.loads(response.text)
    thread_id = response_dict['data']['id']
    print('submitting thread')
    return headers,thread_id

for i in range(7009, 1461094):
    i = i + 1
    try:
        if i % 10 == 0 or i == 1:
            access_token = get_access_token()
        
        webdriver.get(f'https://stackoverflow.com/questions?tab=votes&page={i}')
        print('redirected list of questions')
        sleep(2)

        html = webdriver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)

        hrefs = []

        aTagsInH = webdriver.find_elements(By.CSS_SELECTOR, 'h3 a')
        for a in aTagsInH:
            href = a.get_attribute('href')
            if href.find("https://stackoverflow.com/questions/") != -1:
                hrefs.append(href)

        for link in hrefs:
            webdriver.get(link)
            print('redirected question')
            title = webdriver.find_element(By.CLASS_NAME, 'question-hyperlink').text
            body = webdriver.find_element(By.CLASS_NAME, 'js-post-body').get_attribute('innerHTML')
            
            tags = []
            taged = webdriver.find_elements(By.CLASS_NAME, 'post-tag')
            for tag in taged:
                if(tag.text not in tags):
                    tags.append(tag.text)
            tags = json.dumps(tags)
            answers = webdriver.find_elements(By.CLASS_NAME, 's-prose')
            headers, thread_id = submit_thread(access_token, title, body, tags)
            ans_num = random.randint(3, 20)
            loop = 1
            for answer in answers:
                if(loop <= ans_num):
                    submit_answer(headers, thread_id, answer)
                loop = loop + 1
        print(f'finished {i}. loop')
    except:
        print('Error, restarting again...')
        sleep(4)

