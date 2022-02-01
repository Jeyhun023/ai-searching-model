from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests, json

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# webdriver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options=chrome_options)

webdriver = webdriver.Chrome(ChromeDriverManager().install())
sleep(2)

for i in range(6201, 730082):
    try:
        if i % 10 == 0 or i == 1:
            url = 'https://api.abysshub.com/api/login' # Set destination URL here
            data = {'email': 'creshidov23@gmail.com', 'password': '888ceyhun'}
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":"text/plain"}
            response = requests.post(url, data=data, headers=headers)

            response_dict = json.loads(response.text)
            access_token = response_dict['data']['access_token']
        
        
        webdriver.get(f'https://stackoverflow.com/questions?tab=votes&page={i}')
        sleep(3)

        html = webdriver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)

        hrefs = []

        aTagsInH = webdriver.find_elements_by_css_selector('h3 a')
        for a in aTagsInH:
            href = a.get_attribute('href')
            if href.find("https://stackoverflow.com/questions/") != -1:
                hrefs.append(href)

        for link in hrefs:
            webdriver.get(link)
            title = webdriver.find_element_by_class_name('question-hyperlink').text
            body = webdriver.find_element_by_class_name('js-post-body').get_attribute('innerHTML')
            
            tags = []
            taged = webdriver.find_elements_by_class_name('post-tag')
            for tag in taged:
                if(tag.text not in tags):
                    tags.append(tag.text)
            tags = json.dumps(tags)
            answers = webdriver.find_elements_by_class_name('s-prose')
            
            url = 'https://api.abysshub.com/api/forum/create' # Set destination URL here
            data = {'category_id': 1, 'title': title, 'content' : body, 'tags' : tags}
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":"text/plain", "Authorization": "Bearer " + access_token}
            response = requests.post(url, data=data, headers=headers)
            
            response_dict = json.loads(response.text)
            thread_id = response_dict['data']['id']
            
            ans_num = random.randint(3, 20)
            loop = 1
            for answer in answers:
                if(loop <= ans_num):
                    url = f'https://api.abysshub.com/api/forum/{thread_id}/answer/submit' # Set destination URL here
                    data = {'content' : answer.get_attribute('innerHTML')}
                    requests.post(url, data=data, headers=headers)
                    sleep(2)
                    
                loop = loop + 1
    except:
        print('Error, restarting again...')


