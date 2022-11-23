from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent
import pyautogui

try:
    useragent = UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.chrome}")

    options.add_argument("--disable-blink-features=AutomationControlled")

    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH, options=options)

    url = "https://monkeytype.com/"

    driver.get(url=url)
    print('[+] search')
    sleep(2)

    button_acept = driver.find_element(By.CLASS_NAME, 'button.active.acceptAll').click()
    print('[+] cookie')
    sleep(1)
    modes = driver.find_element(By.ID, 'middle').find_element(By.ID, 'testConfig').find_element(By.CLASS_NAME, 'row').find_element(By.CLASS_NAME, 'mode').find_elements(By.CLASS_NAME, 'textButton')[1].click()
    print('[+] word mode')
    sleep(1)
            
    soup = BeautifulSoup(driver.page_source, 'lxml')
    all_words = soup.find("div", {"id": "words"})
    words_list = []

    for words in all_words:
        text_words = words.text
        words_list.append(text_words)

    full_text = ' '.join(words_list)
    print('[+] full text')
    sleep(1)

    screenWidth, screenHeight = pyautogui.size()
    pyautogui.write(full_text)

    print('[+] writing')
    sleep(1)
    my_list = []
    stats = driver.find_element(By.ID, 'middle').find_element(By.ID, 'result').find_element(By.CLASS_NAME, 'group.raw')
    raw_text = stats.text
    for i in raw_text:
        if i.isdigit():
            my_list.append(i)

    raw = ''.join(my_list)
    print('[+] done')
    sleep(1)

    with open('monkey_type_raw_results.txt', 'a') as monke:
        monke.write(str(raw))
        monke.write('\n')
        monke.close()

    sleep(1)

    driver.close()
    driver.quit()

except Exception as ex:
    print(f'ERROR - {ex}')