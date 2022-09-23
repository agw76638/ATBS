from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox(executable_path=r'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.10\\geckodriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element(By.TAG_NAME, 'html')
message = browser.find_element(By.CLASS_NAME, "game-message").text
over = browser.find_element(By.CLASS_NAME, "game-message")
score = browser.find_element(By.CLASS_NAME, "score-container").text
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

    # TODO Stop program.
    if over:
        print(score)
        browser.quit()