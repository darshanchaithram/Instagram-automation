from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

user_name = "//ENTER YOUR IG USERNAME//"
pass_word = "//ENTER YOUR IG PASSWORD//"

print('Enter chat:')
chat = input()
print("Enter message:")
message = input()

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/")

def Message(user_name,pass_word,chat,message):

    username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username'")))
    password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password'")))
    username.clear()
    password.clear()
    username.send_keys(user_name)
    password.send_keys(pass_word)

    login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'"))).click()
    notnow = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
    notnow2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

    messenger = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'))).click()
    newmsg = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'))).click()
    chat_name = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input'))).send_keys(chat)
    time.sleep(2)

    chat_select = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div[1]'))).click()
    click_next = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button'))).click()
    text_area = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
    time.sleep(2)
    text_area.clear()
    text_area.send_keys(message)
    time.sleep(1)
    text_area.send_keys(Keys.ENTER)

Message(user_name,pass_word,chat,message)
