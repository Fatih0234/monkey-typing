import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from bs4 import BeautifulSoup
import pyautogui

driver_path = os.path.join(os.getcwd(), "chromedriver-win64", "chromedriver.exe")
chrome_service = Service(driver_path)
chrome_options = Options()

browser = Chrome(service=chrome_service, options=chrome_options)
browser.implicitly_wait(7)
browser.maximize_window()

url = "https://monkeytype.com/"

browser.get(url)

# cookies 
cookies = browser.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div[2]/div[2]/button[1]")
cookies.click()
        
        

element_words = browser.find_element(By.ID, "words")
# print(len(element_words.text))
# print(element_words.text) head how where off any home back both may long part however now around part you help person and see long run 

soup = BeautifulSoup(element_words.get_attribute("innerHTML"), "html.parser")
words = soup.find_all("div", "word")
# print(len(words))
# print([w.text for w in words])
       
        
text_block = " ".join([w.text for w in words])

keep_going = True
while keep_going:
    try:
        pyautogui.click(500, 700)
        pyautogui.click(500, 700)
        pyautogui.write(text_block)
        
        old_text_block = text_block
        search_string = old_text_block[-10:]
        print(f"Old text block: {old_text_block}")
        print(f"Search string: {search_string}")
        
        element_words = browser.find_element(By.ID, "words")
        soup = BeautifulSoup(element_words.get_attribute("innerHTML"), "html.parser")
        words = soup.find_all("div", "word")
        text_block = " ".join([w.text for w in words])
        print(f"New text block: {text_block}")

        text_block = text_block[text_block.index(search_string):].replace(search_string, " ")
        print(f"Next text block: {text_block}")  
    except Exception as e:
        print(e)
        keep_going = False
        browser.quit()










# active_word = True
# while active_word:
#     try:
#         active_word = browser.find_element(By.CSS_SELECTOR,".word.active")
#         # let's type the word 
#         action_chains = ActionChains(browser)

#         # get the text of the active word and send it
#         word = active_word.text
#         action_chains.send_keys(word).perform()
#         action_chains.send_keys(Keys.SPACE).perform()
#     except NoSuchElementException as e:
#         print("No such element found")
#         active_word = False
#         browser.quit()
#     except ElementNotInteractableException as e:
#         print("Element is not interactable")
#         active_word = False
#         browser.quit()
#     except Exception as e:
#         print(e)
#         active_word = False
#         browser.quit()
    

