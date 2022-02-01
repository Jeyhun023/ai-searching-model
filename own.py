from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests, json

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
print('loading')
webdriver = webdriver.Chrome(service=Service("/usr/lib/chromium-browser/chromedriver"), options=chrome_options)
# webdriver = webdriver.Chrome(ChromeDriverManager().install())
sleep(2)
print('starting')

def reprocess_body(body): 
    print('reprocessing')
    codes = body.find_elements(By.CSS_SELECTOR, 'pre code')
    count = len(codes)
    
    spans = body.find_elements(By.CSS_SELECTOR, 'pre code span')
    span_counter = len(spans)

    rate = 0 
    
    if(count == 1):
        if(span_counter > 10):
            rate = 5 
        else:
            rate = 4.5
            
    if(count == 2):
        if(span_counter > 25):
            rate = 4  
        else:
            rate = 3.5
            
    if(count == 3):
        if(span_counter > 35):
            rate = 3  
        else:
            rate = 2.5
        
    if(count == 4):
        if(span_counter > 45):
            rate = 2  
        else:
            rate = 1.5
    
    if(count > 4):
        rate = 1
        
    return rate

for i in range(10, 4000):
    try:
        data = requests.get(f'https://dev.to/search/feed_content?per_page=15&page={i}&tag=javascript&sort_by=hotness_score&sort_direction=desc&tag_names%5B%5D=javascript&approved=&class_name=Article').json()
        print('getting list')
        for result in data['result']:
            print('getting question')
            response = webdriver.get(f'https://dev.to{ result["path"] }')
            title = webdriver.find_element(By.CSS_SELECTOR, 'header div h1').get_attribute('innerHTML').strip()

            tags = []
            taged = webdriver.find_elements(By.CLASS_NAME, 'crayons-tag  ')
            for tag in taged:
                tag = tag.text.replace("#\n", "").strip()
                if(tag not in tags):
                    tags.append( tag )
            tags = json.dumps(tags)
            body = webdriver.find_element(By.CLASS_NAME, 'crayons-article__main')
            rate = reprocess_body(body)
            
            url = 'https://reward.az/api/product-bot'
            data = {'title': title, 'body': body.get_attribute('innerHTML'), 'tags' : tags, 'url' : webdriver.current_url, 'rate': rate}
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":"text/plain"}
            requests.post(url, data=data, headers=headers)
            sleep(1)
        print('finished loop')
    except:
        print('Error, restarting again...')
        sleep(1)